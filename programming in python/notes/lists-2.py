def smallest_number(nums):
  '''
  Store a smallest variable
  For each item in the list
    If that item is less than my variable
      Update the variable to item
  Return the smallest variable
  '''
  smallest = nums[0]
  for item in nums:
    if item <= smallest:
      smallest = item
  print(smallest)
  return smallest

# Test cases
smallest_number([8,4]) # 4
smallest_number([-1,3,1,9]) # -1
smallest_number([2,2,2]) # 2