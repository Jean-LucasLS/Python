from itertools import count

c1 = count(start=10, step=2) # 'count()' is both an iterable and an iterator
r1 = range(10) # 'range()' is only a iterable, and not an iterator

print('c1', hasattr(c1, '__iter__'))
print('c1', hasattr(c1, '__next__'))
print('r1', hasattr(r1, '__iter__'))
print('r1', hasattr(r1, '__next__'))

for i in c1:
  if i > 20:
    break
  print(i)