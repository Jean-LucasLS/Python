word = 'dignitas'
given = []

while True:
    letter = input('Digite uma letra: ')
    if len(letter) != 1:
        print('Digitação incorreta.')
        continue
    given.append(letter)
    if letter in word:
        print(f'A letra {letter} está contida na palavra.')
    else:
        print(f'A letra {letter} NÃO está contida na palara.')
        given.pop()
    temporaryletter = ''
    for wordletter in word:
        if wordletter in given:
            temporaryletter += wordletter
        else:
            temporaryletter += '*' # Caso a letra ainda não for digitada, aparecerá um "*".
    if temporaryletter != word:
            print(temporaryletter)
    else:
        print(f'Parabéns, você adivinhou, a palavra é "{word}".')
        break # Função que interrompe o laço.