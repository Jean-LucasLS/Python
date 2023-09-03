def outside(x):
  a = x
  
  def inside(y=0):
    print(locals()) # Shows variables which function 'inside' has access
    print(inside.__code__.co_freevars)
    nonlocal a
    a += 2 + y # It's not possible to change 'a' value if not declared it as 'nonlocal'
    return a
  return inside

inside1 = outside(2)
inside2 = outside(4)


print(inside1(), inside1(2), inside1(), inside2())

print(globals()) # Shows all global variables