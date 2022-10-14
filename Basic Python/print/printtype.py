"""As aspas triplas começam e finalizam
um comentário em mais de uma linha, diferente
do "#" que comenta somente em uma linha
"""
print('10', type('10')) #Entre aspas simples o 10 é tratado como String
print(10, type(10)) #Sem aspas simples o 10 é tratado como int ("10.0" seria considerado float)
print('Jean', type('Jean'))
print(10 == 11, type(10 == 11))
print('L' == 'L', type('L' == 'L'))
print('A' == 'a', type('A' == 'a')) #Sensível a maiúsculo / minúsculo
print('A soma e', 10 + 10) #Operação de soma
print('A juncao e', '10' + '10') #Ao invés de somar, ele "ajunta"
print('Je' + 'an')