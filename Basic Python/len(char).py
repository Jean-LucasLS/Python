char1 = input('Digite algo: ')
char2 = input('Digite outro algo: ')
print(f'A quantidade de caracteres total é {len(char1) + len(char2)}.')
if len(char1) > len(char2):
    print(f'{char1} possui {len(char1)} caracteres, mais caracteres em relação ao {char2}, que possui {len(char2)}.')
elif len(char1) < len(char2): 
    print(f'{char2} possui {len(char2)} caracteres, mais caracteres em relação ao {char1}, que possui {len(char1)}.')
else:
    print(f'{char1} e {char2} possuem ambos {len(char1)} caracteres.')
print('Operação finalizada')