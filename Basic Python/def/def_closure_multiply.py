def operator(op):
  def multiply(num):
    return op * num
  return multiply

double     = operator(2) # It will be saved in the memory of the variable 'double' that the operation will be with the number passed as argument
triple     = operator(3)
quadrupe   = operator(4)

print('number | double() - triple() - quadrupe()')
print(f'->  2  |---- {double(2)} ---|---- {triple(2)} ---|---- {quadrupe(2)} ---|')
print(f'->  5  |--- {double(5)} ---|--- {triple(5)} ---|--- {quadrupe(5)} ---|')
print(f'->  8  |--- {double(8)} ---|--- {triple(8)} ---|--- {quadrupe(8)} ---|')
print(f'-> 10  |--- {double(10)} ---|--- {triple(10)} ---|--- {quadrupe(10)} ---|')