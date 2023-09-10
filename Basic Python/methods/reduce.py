from functools import reduce

products = [
  {'name': 'Product 3', 'price': 10.00 },
  {'name': 'Product 1', 'price': 22.32 },
  {'name': 'Product 5', 'price': 10.11 },
  {'name': 'Product 2', 'price': 105.87},
  {'name': 'Product 4', 'price': 69.90 },
]

# Reduce method
def reduce_func(acumulator, product):
  print(f'acumulator -> {acumulator}')
  print(f'product -> {product}', end='\n\n')
  return acumulator + product['price']

total1 = reduce(
  reduce_func, # lambda ac, p: ac + p['price],
  products, 
  0
)
print(total1)

# 'for' method
total2 = 0
for p in products:
  total2 += p['price']
print(total2)

# List comprehension method
print(sum([p['price'] for p in products]))