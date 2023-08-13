phrase = 'Jucaju is not a DIGNITAS'
print(phrase.split()) # Por padrão, ele separa em itens de listas nos locais em que há espaços (' ')

phrase2 = 'Jucaju-is-not-a-DIGNITAS'
print(phrase2.split()) # Não haverá separação efetiva, e a frase será somente um item da lista, pois não há espaços (' ')

phrase3 = 'Jucaju-is-not-a-DIGNITAS'
print(phrase3.split('-'), end='\n\n') # Especificando o critério de separação, a lista final terá os itens separados ('-')

phrase4 = '        Jucaju is not a DIGNITAS        '
print('#'*4, phrase4, '#'*4)
print('#'*4, phrase4.lstrip(), '#'*4)
print('#'*4, phrase4.rstrip(), '#'*4)
print('#'*4, phrase4.strip(), '#'*4)