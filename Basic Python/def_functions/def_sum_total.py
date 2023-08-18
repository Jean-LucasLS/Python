def sum_total(*args): # O '*' indica que é para empacotar os valores enviados para esta função
  print(f'args: {args}')
  total = 0
  for number in args:
    total += number
  return total

number_sum = sum_total(1, 2, 3) # Passando os valores que serão armazenados em uma 'tuple' ('args')
print(number_sum)

tuple     = (1, 2, 3) # Declarando a 'tuple' que será enviada na função
tuple_sum = sum_total(*tuple) # O asterísco indica que será enviado a tupla desempacotada
print(tuple_sum)