def decorator(func):
  print('Bugger')
  def inner(*args):
    result = func(*args)
    print(f'Result is -> {result}')
    return result
  return inner

@decorator
def sum(x, y):
  print(f'This function\'s name is -> "{sum.__name__}"')
  return x + y

# print(sum(4, 8))

var = sum(2, 4)
print(type(var))