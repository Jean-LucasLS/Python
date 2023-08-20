list = ['Jucaju', 'Jockey', 'DIGNITAS', 'Coney', 'Bylkers']

var1, var2, *rest = list
print(f'var1: {var1} | var2: {var2} | *rest: {rest}\n')

*rest, var1, var2 = list
print(f'*rest: {rest} | var1: {var1} | var2: {var2}\n')

print(*list)