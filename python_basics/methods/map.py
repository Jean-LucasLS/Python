products = [
  {'name': 'Product 3', 'price': 10.00 },
  {'name': 'Product 1', 'price': 22.32 },
  {'name': 'Product 5', 'price': 10.11 },
  {'name': 'Product 2', 'price': 105.87},
  {'name': 'Product 4', 'price': 69.90 },
]

new_products1 = [
  {**p, 'price': round(p['price']*1.1, 2)} for p in products
]

# Map returns an map object, that can be CONSUMED once. If needed, can be convert to a 'list', and it never gets consumed.
new_products2 = map(
  lambda p: {**p, 'price': round(p['price']*1.1, 2)},
  products
)

print(*new_products1, end='\n\n')
print('This is the new_products2 ->', *new_products2) # It gets consumed here
print('This is the new_products2 ->', *new_products2) # Already consumed