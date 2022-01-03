DELTAS = [(0, 1), (-1, 0), (0, -1), (1, 0)]
# Down, Right, Up Left


def print_maze(maze):
  for row in maze:
    print("".join(row))
  print("---")


def read_maze(filename):
  with open(filename, "r") as f:
    lines = f.readlines()
    maze = [list(l.strip()) for l in lines]
  return maze


def find_start(maze):
  start = None
  for i, row in enumerate(maze):
    for j, cell in enumerate(row):
      if cell == "S":
        start = (i, j)
  return start


def solve(maze):
  def look(x, y, maze):
    # Base case: check if we're in bounds
    if x not in range(len(maze)) or y not in range(len(maze[0])):
      return False
    # Base case: we've found the end
    if maze[x][y] == "E":
      return True
    # Base case: we hit a wall or visited
    if maze[x][y] in ["1", "2", "."]:
      return False

    # Mark current cell as visited
    maze[x][y] = "."
    print_maze(maze)

    # Try all 4 directions
    found_solution = False
    for dx, dy in DELTAS:
      found_solution = found_solution or look(x + dx, y + dy, maze)

    if found_solution:
      return True
    else:  # Hit a dead end
      maze[x][y] = "2"  # Mark dead end paths as visited
      return False

  sx, sy = find_start(maze)
  solution = look(sx, sy, maze)
  # Clean up the maze
  maze[sx][sy] = "S"
  #maze = [["0" if c == "2" else c for c in row] for row in maze]
  return (solution, maze)


#maze1 = read_maze("E:\Dropbox\Classroom\courses\seminar\maze\maze.txt")
maze1 = read_maze("/Users/lee/Dropbox/Classroom/courses/seminar/topics/maze/maze.txt")
sol, maze1 = solve(maze1)
print(sol)
print_maze(maze1)
