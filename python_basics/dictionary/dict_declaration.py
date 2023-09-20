corresp1 = {'Jucaju': 'DIGNITAS',
            'Ad': 'Omnem', 
            'Dodger': {'Jockey': 'Cacetiff',
                       'Nolpsy': 'Bombocayne'}
            }

print(corresp1, type(corresp1))
print(corresp1['Dodger'], corresp1['Dodger']['Jockey'], '\n')

#### Another way to declare a dict ####

corresp2 = dict(Jucaju='DIGNITAS', Ad='Omnem', Dodger=dict(Jockey='Cacetiff', Nolpsy='Bombocayne'))

print(corresp2, type(corresp2))
print(corresp2['Dodger'], corresp2['Dodger']['Jockey'], '\n')