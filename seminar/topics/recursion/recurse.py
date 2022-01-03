def length(l):
  if not l:
    return 0
  return 1 + length(l[1:])

def digsum(num):
  if num < 10:
    return num
  return num % 10 + digsum(num//10)

def rsum(l):
  if not l:
    return 0
  return l[0] + rsum(l[1:])

def fib(n):
  if n == 0:
    return 0
  if n == 1:
    return 1
  return fib(n-2) + fib(n-1)

nums = [28, 19, 120, 16]

assert length(nums) == len(nums)
assert rsum(nums) == sum(nums)
assert digsum(1234) == 10
assert fib(8) == 21
