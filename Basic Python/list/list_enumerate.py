list      = ['Jucaju', 'Jockey', 'DIGNITAS', 'Coney', 'Bylkers']
enum_list = enumerate(list) # Convert the argument to a tuple iterator

print(enum_list, type(enum_list))

for item in enum_list:
  print(item)
  
for item in enum_list: # On the second attempt to iterate it, it will not work, as it will already be 'consumed'
  print(item)
  
print('')

for item in enumerate(list): # A possible solution is to use the 'enumerate' function in a 'for' loop
  print(item)
  
print('')
  
for index, char in enumerate(list): # Unpacking declared in the 'for' loop
  print(f'index: {index} | char: {char}')