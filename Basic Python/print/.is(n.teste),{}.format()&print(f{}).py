name = input('Digite algo: ')
n = name
print(n.isnumeric()) #verificar se é somente numérico
print(n.isalnum()) #verificar se é alfanumérico
print(n.isalpha()) #verificar se há somente letras (espaços geram negação)
print('O {} e {} foram igualados.'.format(n, name)) #Utilização do "format"
print(f'o {n} e {name} foram igualados') #Print com o format como "f" no começo do print