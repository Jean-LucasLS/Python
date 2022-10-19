v = [5, 3, 4, 1, 2]
list = ['2', '3', '5', '1', '4']
letter = ['B', 'Z', 'D', 'T', 'A']
v.sort() # A função "sort()" coloca o vetor "v" em ordem crescente.
list.sort(reverse=True) # A função "sort(reverse=True)" coloca a lista "list" em ordem decrescente.
letter = sorted(letter) # A função "sorted()" faz com que "letter" tenha as letras colocadas em ordem alfabética (crescente). 
for i in range(len(v)):
    print(v[i], end=' ')
print()
for i in range(len(list)):
    print(list[i], end=' ')
print()
for i in range(len(letter)):
    print(letter[i])
