def sum_total(*args): # The '*' indicates that it is to package the values sent to this function
  print(f'args: {args}')
  total = 0
  for number in args:
    total += number
  return total

number_sum = sum_total(1, 2, 3) # Passing the values that will be stored in a 'tuple' ('args')
print(number_sum)

tuple     = (1, 2, 3) # # Declaring the 'tuple' that will be sent in the function
tuple_sum = sum_total(*tuple) # The '*' indicates that the unpacked tuple will be sent
print(tuple_sum)