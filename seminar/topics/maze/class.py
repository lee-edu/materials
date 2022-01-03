@memoize
def length(l):
  # Base case
  if not l:
    return 0
  # Recursive case
  return 1 + length(l[:-1])



nums = [10,11,14,13]
assert length(nums) == len(nums)

nums[a:b] #List subset / access notation
nums[1:3]

length([1,2,3,4])
  >>> 1 + length([1,2,3])
            >>> 1 + length([1,2])
                      >>> 1 + length([1])
                              >>> 1 + length([])
                                      >>> 0
