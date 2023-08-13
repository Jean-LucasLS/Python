list      = ['Jucaju', 'Jockey', 'DIGNITAS', 'Coney', 'Bylkers']
enum_list = enumerate(list) # Converte o argumento em um iterator de tuples

print(enum_list, type(enum_list))

for item in enum_list:
  print(item)
  
for item in enum_list: # Na segunda tentativa de iterálo, não funcionará, pois ele já estará 'consumido'
  print(item)
  
print('')

for item in enumerate(list): # Uma possível solução é utilizar a função 'enumerate' já num laço 'for'
  print(item)
  
print('')
  
for index, char in enumerate(list): # Desempacotamento declarado no laço 'for'
  print(f'index: {index} | char: {char}')