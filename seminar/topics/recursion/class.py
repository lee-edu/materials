def look(x,y):
  check in 4 directions
  # Base case
  When you see the E
    Return yes solution
  # Base case
  When you only see 1s
    Return no solution
  # Recursive
  When you see a 0
    look(that direction)
  if look returned Yes solution:
    Return the path / there's a solution
  else:
    No path


look(sx, sy)