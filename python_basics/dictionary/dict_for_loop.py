dict = {'Jucaju': 'DIGNITAS',
        'Dodger': {'Willford': 'Snowpiercer',
                   'Doc': 'Barricade'},
        'Jockey': 'Bylkers'
        }

print('keys -> ', end='')
for key in dict:
  print(key, end=' ')
  
print('\n\nvalues -> ', end='')
for value in dict.values():
  print(value, end=' ')
  
print('\n')
for key, value in dict.items():
  print(f'key -> {key} | value -> {value}')