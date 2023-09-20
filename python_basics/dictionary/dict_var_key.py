dict = {'Jucaju': 'DIGNITAS',
        'Dodger': {'Willford': 'Snowpiercer',
                   'Doc': 'Barricade'}
        }

dict['Lump'] = 'Bylkers' # Add a new key-value to dict
dict['Dodger']['Dex'] = 'Mug' # Add a new key-valie to a dict inside another dict

key       = 'Dyield'
dict[key] = 'Stock'

print(dict, f'dict[key]: {dict[key]} | dict["Dyield"]: {dict["Dyield"]}', sep='\n')