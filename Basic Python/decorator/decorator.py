#### Syntax Sugar ####

def decorator(func):
  def inner(*args):
    result = func(*args)
    print(f'Result was "{result}"')
    return result
  print('Lockwood')
  return inner

'''Python will execute the decorator function inside
content right after the '.py' file execution. This doest
no happen for functions inner the decorator ('def inner')'''
@decorator
def string_invert1(string):
  print(f'This function is "{string_invert1.__name__}"')
  return string[::-1]

# Closure without decorator
def string_invert2(string):
  print(f'This function is "{string_invert2.__name__}"')
  return string[::-1]  

# Using the '@' + the name of the decorator, it's possible to use the target function directly
invertion1 = string_invert1('ujacuJ')
print(invertion1)

# This would be the step-by-step without a '@' + decorator
invertion2 = decorator(string_invert2)
print(invertion2('ujacuJ'))