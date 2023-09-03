def decorator_parameters(name):
  def decorator(func):
    print('Decorator ->', name)
    def new_function(*args, **kwargs):
      result = func(*args, **kwargs)
      final  = f'{result} {name}'
      return final
    return new_function
  return decorator

@decorator_parameters(name='third')
@decorator_parameters(name='second')
@decorator_parameters(name='first')
def sum(x, y):
  return x + y

ten_plus_five = sum(10, 5)
print(ten_plus_five)