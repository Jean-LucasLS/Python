name = input('Digite algo: ')
n = name
print(n.isnumeric()) # Verificar se é somente numérico
print(n.isalnum()) # Verificar se é alfanumérico
print(n.isalpha()) # Verificar se há somente letras (espaços geram negação)
print('O {} e {} foram igualados.'.format(n, name)) # Utilização do 'format' no final
print(f'o {n} e {name} foram igualados')