products = [
  {'name': 'Product 3', 'price': 10.00 },
  {'name': 'Product 1', 'price': 22.32 },
  {'name': 'Product 5', 'price': 10.11 },
  {'name': 'Product 2', 'price': 105.87},
  {'name': 'Product 4', 'price': 69.90 },
]

new_products1 = [
  p for p in products
  if p['price'] > 10
]

# Using lambda
new_products2 = filter(
  lambda p: p['price'] > 10,
  products
  )

# Using a declared function
def price_filter(product):
  return product['price'] > 10

new_products3 = filter(
  price_filter,
  products
)

print(*new_products1)
print(*new_products2)
print(*new_products3)