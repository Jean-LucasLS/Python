def sum(x, y):
  return x + y

def multiply(x, y):
  return x * y

def divide(x, y):
  return y / x

def execute(func, x):
  def intern(y):
    return func(x, y)
  return intern

double   = execute(multiply, 2)
triple   = execute(multiply, 3)
sum_2    = execute(sum, 2)
sum_16   = execute(sum, 16)
divide_2 = execute(divide, 2)
divide_5 = execute(divide, 5)

print(sum_16(16))
print(divide_5(10)) 