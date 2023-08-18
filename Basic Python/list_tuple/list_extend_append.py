list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list2 + list1 # A ordem da soma das listas importa
list4 = list(range(1, 10, 2)) # Criação de uma lista que vai do número 1 ao 10, pulando de 2 em 2.
print(list4); print(list3)

list3 = list1 + list2
print(list3)

list2.extend(list1) # A função extend adiciona "list1" ao conteúdo da "list2"
print(list2)

list1.append(4) # Funçao que adiciona um item ao final da lista.
print(list1)

list1.insert(0, 'test') # Função que insere, no índice indicado, o conteúdo descrito. (list[0] -> 'teste')
print(list1)

del(list1[3]) # Função que remove o que contém no índice mencionado.
print(list1)