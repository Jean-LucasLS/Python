def decorator_factory(k=None, w=None):
  print('Decorator Factory', end= ' | ')
  def function_factory(func):
    print('Function Factory', end=' | ')
    def inner(*args, **kwargs):
      print('Inner')
      res = func(*args, **kwargs)
      return res
    return inner
  return function_factory

@decorator_factory(k=None, w=None)
def sum(x, y):
  return x + y

sum_1 = sum(1, 2)
print(sum_1)

# The first parentesis pass the 'dec_factory' arguments, and the second, 'func_factory'
multiply1 = decorator_factory(k=2, w=4)(lambda x, y: x * y) 
print(multiply1(2, 4), multiply1(8, 8))

# This is the same declaration than 'multiply1'
decorator = decorator_factory()
multiply2 = decorator(lambda a, b: a * b) 
print(multiply2(1, 2), multiply2(8, 8))
