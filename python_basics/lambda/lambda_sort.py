l1 = [3, 2, 4, 1, 6, 5, 8, 7]
l1.sort(reverse=True) # This method can put values in order
print(l1)

#### Sorting 'char' dicts ####

l2 = [
  {'name': 'Jucaju' , 'lastname': 'DIGNITAS'},
  {'name': 'Joseph' , 'lastname': 'Willford'},
  {'name': 'Bylkers', 'lastname': 'Dorigon' },
  {'name': 'Hominem', 'lastname': 'Druckey' }
]

# Declaring function
l3 = l2.copy()
def order(item):
  return item['name']

l2.sort(key=order)
print(l2)

# Using 'lambda' function
l4 = l2.copy()
l4.sort(key=lambda item: item['name'])
print(l4)
