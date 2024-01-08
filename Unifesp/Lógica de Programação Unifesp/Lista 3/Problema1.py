nome = ['Maria', 'Joao', 'Antonio', 'Roberta', 'Carla'] #Jean-Lucas Luquetti Silva / RA: 120443
sobrenome = ['Silva', 'Pereira', 'Costa', 'Santos', 'Soares'] #Declaração das duas listas, nome e sobrenome
for i in range(5): #laço para ir somando os mesmos termos das listas e depois imprimindo as somas
	soma = len(nome[i]) + len(sobrenome[i]) #uso de "len" para dizer o número de caracteres da string
	print(soma)
