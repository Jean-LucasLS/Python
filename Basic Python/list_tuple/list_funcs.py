list = ['Jucaju', 3, 43.3]

del list[2] # Deleta o elemento especificado, fazendo com que os elementos à frente retrocedam em uma unidade os seus índices atuais
print(list, end='\n\n')

list.append([111, 'Jockey']) # Adicionando uma lista como um elemento de outra lista
print(f'{list} | {list[2]} type is {type(list[2])}', end='\n\n')

del_last = list.pop() # Salvando o último elemento removido da lista que fora removido pelo método 'pop'
print(f'list: {list} | pop: {del_last}', end='\n\n')

list.insert(1, 'Cajuca') # O método 'insert' recebe (índice_lista, elemento_para_adicionar)
print(list, end='\n\n')

list.insert(50000000, 'DIGNITAS') # Caso o índice ultrapasse o tamanho da lista, o elemento será adicionado após o maior índice atual
print(f'list: {list} | list[4]: {list[3]} | list[50000000]: IndexError: list index out of range', end='\n\n')

list2 = ['Mojito', 22, 'Totem'] # Junção de duas listas através da operação '+'
print(f'list + list2 = {list + list2} | list2 + list = {list2 + list}', end='\n\n')

list.extend(list2) # A função 'extend' necessariamente altera a lista que chama o método, não podendo armazenar em uma terceira variável
print(f'list.extend(list2) = {list}')