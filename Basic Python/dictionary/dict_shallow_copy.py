d1 = {
  'Jucaju': 'DIGNITAS',
  'list': [0, 1, 2]
}

d2            = d1.copy() # This method makes a shallow copy, unbinding only imutable values
d2['Jucaju']  = 'Omnem' # This value will not be changed in d1, only d2
d2['list'][0] = 2 # The type 'list' is mutable, so it will change d1 list too
print(d1, d2, sep='\n')

#### Deep copy ####

import copy

d3 = {
  'Jucaju': 'DIGNITAS',
  'list': [0, 1, 2]
}

d4            = copy.deepcopy(d3)
d4['Jucaju']  = 'Omnem'
d4['list'][0] = 2 #
print(d3, d4, sep='\n')