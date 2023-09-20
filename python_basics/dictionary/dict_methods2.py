dict = {'Jucaju': 'DIGNITAS',
        'Dodger': {'Willford': 'Snowpiercer',
                   'Doc': 'Barricade'},
        'BigJohn': 'Bylkers',
        'Ad': 'Hominem'
        }

#### 'pop' method ####

specific_value = dict.pop('Dodger') # Drop a specific key-value in the dict
last_value     = dict.popitem() # Drop the last key-value in the dict

print(f'pop -> {specific_value} | popitem -> {last_value}')
print(dict)

#### 'update' method ####

dict.update({ # This method changes and add values. Values that was not declared still unchanged
  'Jucaju': 'Team-DIGNITAS',
  'Dodger': 'Los Alamos',
  'Willford': 'Snowpiercer'
})
print(dict)

dict.update(Jucaju='DIG', # Another way to use 'update' method is passing key-values as arguments
            Dodger='LA',
            JW='Big Alice',
            John='Isidore') 
print(dict)

tuple = (('C4', 'Jhin'), ('Lup', 'MZion')) # Passing a tuple or a list is another option too
dict.update(tuple); print(dict)

list  = [['Dux', 'Dex'], ['Doc', 'Barricade']]
dict.update(list); print(dict)