product = {
  'name': 'Blue Pen',
  'price': 2.5,
  'category': 'Office'
}

# print(product.items())
# for key, value in product.items():
#   print(key, value)

dc1 = {
  key.title(): value.upper()
  if isinstance(value, str) else value
  for key, value
  in product.items()
  if key != 'category'
}
print(dc1)

#### Convert list to dict ####

list = [
  ('a', 'value a'),
  ('b', 'value b'),
  ('c', 'value c')
]
print(dict(list))

dc2 = {
  key: value
  for key, value in list
}
print(dc2)