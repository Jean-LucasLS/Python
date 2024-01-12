dict = {'Jucaju': 'DIGNITAS',
        'Dodger': {'Willford': 'Snowpiercer',
                   'Doc': 'Barricade'},
        'Non-existing': 'To-be-deleted'
        }

print(f'dunder: {dict.__len__()} | method: {len(dict)}')
print(dict.keys(), dict.values(), dict.items(), sep='\n')

#### 'get' method ####

del dict['Non-existing']

if dict.get('Non-existing') is None:
  print('This key does not exist')
  
dict.get('Non-existing', print('This key does not exist')) # If the method 'get' doest not found the passed key, it execute the second argument.
if dict.get('Non-existing', True):
  print('This key does not exist')
  
#### The method 'setdefault()' add a key-value only if they doest not exist. If exists, it does nothing. ####

dict.setdefault('Jucaju', 'Non-DIGNITAS')
print(dict['Jucaju']) # It did nothing, because 'Jucaju' already has a key-value.

dict.setdefault('BigJohn', 'Bylkers')
print(dict) # Considering that 'BigJohn' was not already a key, it has been added to dict with a value



