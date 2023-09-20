import pprint

def p(v):
  pprint.pprint(v, sort_dicts=False, width=40)

products = [
  {'name': 'p1', 'price': 20},
  {'name': 'p2', 'price': 10},
  {'name': 'p3', 'price': 30}
]

new_products1 = [
  {'name': product['name'], 'price': product['price']}
  for product in products
]
print(*new_products1, sep='\n', end='\n\n')

new_products2 = [
  {**product, 'price': product['price'] * 1.05} # It's possible to modify a specific key-value after unpacking a dict
  if product['price'] > 20 else {**product}
  for product in products
]
print(*new_products2, sep='\n')
p(new_products2)