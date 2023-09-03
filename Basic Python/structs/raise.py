print(123)
# raise ValueError('Error')
print(456)

def zero_test(d):
  if d == 0:
    raise ZeroDivisionError('Trying a divison by zero.')
  return True

def int_float_test(n):
  type_n = type(n)
  if not isinstance(n, (float, int)):
    raise TypeError(f'"{n}" must be int or float, and it\'s "{type_n.__name__}".')
  return True

def divide(n, d):
  int_float_test(n)
  zero_test(d)
  return n / d

print(divide({2, 3}, 1))