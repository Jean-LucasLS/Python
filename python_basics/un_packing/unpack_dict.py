# x, y = 1, 2; x, y = y, x; print(x, y)

person = {
  'name': 'Jucaju',
  'lastname': 'DIGNITAS'
}

a, b = person
c, d = person.values()
print('keys: {a}, {b} | values: {c}, {d}')

c1, d1 = person.items()
print(c1, d1)

(a1, a2), (b1, b2) = person.items()
print(f'{a1} -> {a2}, {b1} -> {b2}')