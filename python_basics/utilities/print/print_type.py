'''As aspas triplas começam e finalizam
um comentário em mais de uma linha, diferente
do '#' que comenta somente em uma linha
'''
print('10', type('10')) # Between quotes, 10 is treated as a String
print(10, type(10)) # Without quotes, 10 is treated as an int ('10.0' would be considered a float)
print('Jean', type('Jean'))
print(10 == 11, type(10 == 11))
print('L' == 'L', type('L' == 'L'))
print('A' == 'a', type('A' == 'a')) # Case sensitive
print('A soma e', 10 + 10) # Sum operation
print('A juncao e', '10' + '10') # Instead of adding, it 'joins'
print('Je' + 'an')