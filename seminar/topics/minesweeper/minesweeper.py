from random import randint as roll


class Tile:
    """
    The Tile class keeps track of individual Minesweeper tiles
    """

    def __init__(self, grid, x, y):
        self.is_mine = False
        self.nearby_mines = 0
        self.hidden = True
        self.marked = False
        self.grid = grid
        self.x = x
        self.y = y

    def __repr__(self):
        if self.marked:
            return "⚑"
        if self.hidden:
            return "☐"
        return "⚙" if self.is_mine else str(self.nearby_mines)

    def count_mines(self):
        neighbors = self.get_neighbors()
        self.nearby_mines = len([1 for tile in neighbors if tile.is_mine])

    def mark(self):
        self.marked = not self.marked

    def reveal(self):
        if not self.hidden:  # Don't do anything if revealed already
            return self.is_mine
        self.hidden = False
        # Reveal all neighbors if 0
        if self.nearby_mines == 0 and not self.is_mine:
            neighbors = self.get_neighbors()
            for tile in neighbors:
                tile.reveal()
        return self.is_mine

    def get_neighbors(self):
        neighbors = []
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                # Skip self
                if dx == 0 and dy == 0:
                    continue
                cx = self.x + dx
                cy = self.y + dy
                if self.grid.check_coordinates(cx, cy):
                    neighbors.append(self.grid.grid[cx][cy])
        return neighbors


class Grid:
    """
    The Grid class keeps track of the Minesweeper grid in a 2D list of Tiles
    """

    def __init__(self, n, m, num_mines):
        self.n = n
        self.m = m
        self.num_mines = num_mines
        self.grid = None
        self.generate_grid()

    def render(self):
        # Print the coordinate axes
        print(" " * 4, end="")
        print("|".join([str(i) for i in range(self.m)]))
        print()

        for idx, row in enumerate(self.grid):
            print(idx, end=" " * 3)
            print("|".join([repr(cell) for cell in row]))

    def generate_grid(self):
        """
            Create an n x m 2d list w/ num_mines randomly generated and each tile is labeled correctly
            """
        self.grid = [
            [Tile(self, i, j) for j in range(self.m)] for i in range(self.n)
        ]
        self.generate_mines()
        self.label_tiles()

    def generate_mines(self):
        """
            Add num_mines mines to the grid
            """
        for i in range(self.num_mines):
            # Generate non-mine coord
            x, y = roll(0, self.n - 1), roll(0, self.m - 1)
            while self.grid[x][y].is_mine:
                x, y = roll(0, self.n - 1), roll(0, self.m - 1)
            # Set the chosen coord as mine
            self.grid[x][y].is_mine = True

    def label_tiles(self):
        """
            Label each non-mine tile with the number of mines in its 8 neighboring tiles
            """
        for x, row in enumerate(self.grid):
            for y, tile in enumerate(row):
                if tile.is_mine:
                    continue
                tile.count_mines()

    def check_mines_marked(self):
        all_marked = True
        for row in self.grid:
            for tile in row:
                if tile.is_mine and not tile.marked:
                    all_marked = False
        return all_marked

    def check_coordinates(self, x, y):
        return x in range(self.n) and y in range(self.m)

    def mark(self, x, y):
        self.grid[x][y].mark()

    def reveal(self, x, y):
        return self.grid[x][y].reveal()


class Minesweeper:
    """
      Handles player input loop & maintains grid
      """

    def __init__(self):
        difficulty = self.ask_difficulty()
        print("Generating grid...")
        self.grid = Grid(*difficulty)
        self.playing = True
        self.grid.render()

    def ask_difficulty(self):
        difficulty = input(
            "Which difficulty would you like?\t[E]asy\t[M]edium\t[H]ard\n").lower()
        while difficulty not in ["e", "m", "h"]:
            print("Sorry, please choose one of the following options:")
            difficulty = input("[E]asy\t[M]edium\t[H]ard\n").lower()
        if difficulty == "e":
            return (4, 6, 3)
        if difficulty == "m":
            return (8, 9, 12)
        if difficulty == "h":
            return (9, 9, 15)

    def play(self):
        revealed_mine = self.handle_player_input()
        self.grid.render()
        self.check_game_end(revealed_mine)

    def handle_player_input(self):
        # Get player action
        action = input(
            "Please select an action:\t[M]ark/unmark a coordinate\t[R]eveal a tile.\n"
        ).lower()
        while action not in ["m", "r"]:
            action = input(
                "Invalid input.\nPlease select an action:\t[M]ark/unmark a tile\t[R]eveal a tile.\n"
            ).lower()
        # Get coordinates of tile
        coordinates = self.get_coordinates()
        while not self.grid.check_coordinates(*coordinates):
            print("Invalid input.")
            coordinates = self.get_coordinates()
        # Resolve action
        if action == "m":
            self.grid.mark(*coordinates)
            return False
        if action == "r":
            return self.grid.reveal(*coordinates)

    def get_coordinates(self):
        coordinates = input(
            "Please input coordinates in the format x,y\tx goes down, y goes across\n"
        )
        return [int(coord) for coord in coordinates.split(",")]

    def check_game_end(self, revealed_mine):
        # Check if player revealed a mine
        if revealed_mine:
            print("You revealed a mine! Game over :(")
            self.playing = False
        # Check if player marked all mines
        won = self.grid.check_mines_marked()
        if won:
            print("You marked all the mines! Congratulations!")
            self.playing = False

    def ask_play_again(self):
        play_again = input("Do you want to play again?\t[Y]es / [N]o\n")
        return "y" in play_again.lower()


def play_minesweeper():
    game = Minesweeper()
    while game.playing:
        game.play()
    if game.ask_play_again():
        play_minesweeper()


if __name__ == "__main__":
    play_minesweeper()
