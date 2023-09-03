''' #### Tasks ####
1 -> Apply an increase of 10% in prices
2 -> Sort by names descending
3 -> Sort by prices ascending'''

products = [
  {'name': 'Product 3', 'price': 10.00 },
  {'name': 'Product 1', 'price': 22.32 },
  {'name': 'Product 5', 'price': 10.11 },
  {'name': 'Product 2', 'price': 105.87},
  {'name': 'Product 4', 'price': 69.90 },
]

#### Task 1 ####
new_products = [
  {**dict, 'price': round(dict['price'] * 1.1, 2)}
  for dict in products
]

#### Task 2 ####
# Sort method 1
name_sorted_products = sorted(
  new_products, #copy.deepcopy(new_products)
  key=lambda item: item['name'],
  reverse=True
)

# Sort method 2
import copy
name_sorted_products = copy.deepcopy(new_products)
name_sorted_products.sort(key=lambda item:item['name'], reverse=True)

#### Task 3 ####
# Sort method 1
price_sorted_products = sorted(
  new_products,
  key=lambda item:item['price']
)

# Sort method 2
price_sorted_products = copy.deepcopy(new_products)
price_sorted_products.sort(key=lambda item:item['price'], reverse=False)

print(f'10% increase -> {new_products}')
print(f'name sort descending -> {name_sorted_products}')
print(f'price sort ascending -> {price_sorted_products}')