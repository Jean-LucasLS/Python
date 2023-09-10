from itertools import combinations, permutations, product

def print_iter(iterator):
  print(*list(iterator))

people = ['Jucaju', 'DIGNITAS', 'Willford', 'Doc']
shirts = [
  ['blue', 'yellow'],
  ['P', 'M', 'G'],
  ['male', 'female']
]

# print_iter(combinations(people, 2))
# print_iter(permutations(people, 2))
print_iter(product(*shirts))