num1 = input('Digite um numero: ')
while num1.isnumeric() != True: #Será repetido o "input" até que seja verdadeiro a condição de "num1" ser numérico.
    num1 = input('Digite NUMERO: ') #O código não sairá do laço "while" até ser fornecido uma variável SOMENTE numérica.
print(f'O número digitado é {num1}')