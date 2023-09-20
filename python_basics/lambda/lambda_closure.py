def execute(func, *args):
  return func(*args)

def sum(x, y):
  return x + y

print(f'def -> {execute(sum, 2, 6)}  | lambda -> {execute(lambda x, y: x + y, 2, 6)}')

def operator(op):
  def multiply(num):
    return op * num
  return multiply

func_double = operator(2)
lamb_double = execute(lambda op: lambda num: op * num, 2)

print(f'def -> {func_double(8)} | lambda -> {lamb_double(8)}')