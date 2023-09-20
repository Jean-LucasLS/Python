import os

list = [0, 1, 2, 3]

command = 'start'

while command != 'e':
  print(f'Current list: {list}')
  print('[a]dd | [r]emove | [e]xit')
  command = input('Digit the command: ')

  if command == 'a':
    os.system('cls')
    try:
      add_index   = int(input('Digit the index  to be added: '))
      data_to_add = int(input('Digit the number to be added: '))
      list.insert(add_index, data_to_add)
      os.system('cls')
    except ValueError:
      os.system('cls')
      print('It\'s not a valid number. Please try again.')

  elif command == 'r':
    try:
      os.system('cls')
      print(f'Current list: {list}')
      del_index = int(input('Digit the index to be removed: '))
      del list[del_index]
    except IndexError:
      os.system('cls')
      print('It\'s not a existing index. Please try again.')

  elif command == 'e':
    os.system('cls')
    print(f'{list}\nGood bye.')
    
  else:
    os.system('cls')
    print('It\'s not a valid command.')