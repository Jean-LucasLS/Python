name = input('Digite algo: ')
n = name
print(n.isnumeric()) #verificar se é somente numérico
print(n.isalnum()) #verificar se é alfanumérico
print(n.isalpha()) #verificar se há somente letras (espaços geram negação)
print('O {} e {} foram igualados.'.format(n, name))
