import sys

iterable1  = ['I', 'have', '__iter__']
iterable1 = iterable1.__iter__() # Has __iter__ and __next__
print(next(iterable1))
print(next(iterable1))
print(next(iterable1))

iterable2 = ['I', 'have', '__iter__']
iterable2 = iter(iterable2) # Has __iter__ and __next__
list_comp = [n for n in range(50)]
generator = (n for n in range(50)) # Generator object

print(list_comp) # List values are taking up so much memory space
print(generator) # Generator gives only one value at a time (when asked)

# List is taking up much more memory compared to the generator
print(sys.getsizeof(list_comp))
print(sys.getsizeof(generator))

# for i in generator:
#   print(i)