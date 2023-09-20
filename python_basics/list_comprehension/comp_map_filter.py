list = [n for n in range(10) if n < 5] # 'if" has been applied after the 'for' loop
print(list)

products = [
  {'name': 'p1', 'price': 20},
  {'name': 'p2', 'price': 10},
  {'name': 'p3', 'price': 30}
]

new_products = [
  {**product, 'price': product['price'] * 1.05} 
  if product['price'] > 20 else {**product} # Mapping (before 'for' loop)
  for product in products
  if product['price'] >= 20 and (product['price'] * 1.05) > 10 # Filtering (after 'for' loop)
]
print(*new_products, sep='\n')