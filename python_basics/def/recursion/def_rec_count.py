import sys

# n = 9
# sys.setrecursionlimit(n) # If the recursion exceeds 'n', it returns RecursionError

def recursion(init=0, end=10):
  print(init)
  init += 1
  if init <= end:
    return recursion(init, end)
  return

recursion()