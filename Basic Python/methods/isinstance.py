list = ['a', 1, 1.1, True, [0, 1, 2], (1, 2), {0, 1}, {'name': 'Jucaju'}]

# types = [type(item) for item in list]
# print(types)

for item in list:
  if isinstance(item, set):
    item.add(5)
    print(item)
  elif isinstance(item, str):
    item.upper() # Does nothing, 'cause 'str' is imutable
    print(item)
    print(item.upper())
  elif isinstance(item, (int, float)):
    item *= 10
    print(item)
  else:
    print(type(item))