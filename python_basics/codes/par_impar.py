number = input('Digit a number: ')
if number.isdigit():
  number = int(number)
  if number % 2 == 0:
    print('Par')
  else:
    print('Ímpar')
else:
  print('Its not a integer number')