# Minesweeper
You will be working in pairs (or trios) to code [Minesweeper](https://en.wikipedia.org/wiki/Minesweeper_(video_game)) from scratch.

## Objectives
This project will assess your ability to:
  - Write algorithms involving 2D data structures
  - Compose your code into functions
  - Professionally document your code
  - Write code that handles user input

## Task
Use any language to write Minesweeper. The game is described as follows:

1. Generate an `n` by `m` grid. There are `k` mines randomly placed on this grid, and each non-mine tile is labeled with the number of mines located in its 8 neighboring tiles.
2. The player has 3 actions: they can reveal a tile, mark a tile, or unmark a tile.
   1. Revealing a non-mine tile will show the number label of that tile
      1. Revealing a mine will end the game, and the player loses
      2. If the player reveals a tile with 0 neighboring mines, all adjacent non-mine tiles will automatically be revealed. This can cause a chain reaciton if another 0 is revealed as a result.
   2. Marking a tile will visually label the tile with a marker, but will not reveal the contents of that tile.
   3. Unmarking a tile will remove the visual marker from a tile.
3. The player wins when all `k` mines have been marked correctly.

This is also the rough order in which you should write the code! The chain reacton for unrevealing a 0 will be quite tricky.

If you finish early, feel free to add flavor text, find ASCII art, figure out a GUI -- whatever you come up with!

Each group will be presenting their game next week.

## Hints
- Start with figuring out an internal data structure to keep track of the state of the grid.
- Be careful with indexes! What happens if an index goes out of bounds?
- A Tile class might come in handy! What properties might a Tile want to remember?
- Remember to comment your code as you go along!
- Git will be useful for async code collaboration.

## Write-up
As you are working on the code, keep these prompts in mind! You will be writing a blog-style response for this project.

1. Describe how the members of your group collaborated.
2. Describe the data structures you used. Did you make a 2d list? Use a dictionary? Make new classes? etc
3. What challenges did your group face, and how did you overcome these challenges?
4. Which part of the code are you the most proud of, and why?
5. Explain your group's solution to the 0 chain reaction.

## Milestones
You have a week to work on this project; here is a rough timeline that might be helpful:
  - Day 1: Generate an `n` by `m` grid with `k` mines
  - Day 2: Allow a user to reveal, mark, and unmark tiles
  - Day 3: Allow a user to win if they correctly mark all `k` tiles
  - Day 4: Figure out the 0 chain reaction code
  - Day 5: Test your code! Play some Minesweeper! **COMMENT YOUR CODE!**
  - Day 6: Respond to the write-up prompts
  - Day 7: Test and **proofread your comments**!

## Submission
On Google Classroom, one person from each group should turn in:
  - a Google Doc, Markdown, or txt file that contains your responses to the above prompts
  - any code that you wrote for this project (if multiple files, please compress into a `.zip`)
  - cited sources and names!