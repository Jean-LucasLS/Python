idade1 = 18
idade2 = 15
check1 = (idade1>=18) 
check2 = (idade2>=18)
message = 'Reset AutoAttack' if check1 else 'AutoAttack Reset'
print(message)
message = 'Reset AutoAttack' if check2 else 'AutoAttack Reset'
print(message)

"""Caso a condição no parêntesis seja atendida, "check1" recebe o valor de "idade1",
tornando-se um um valor, portanto assumindo uma condição verdadeira. A mesma
condição se aplica para "check2", relacionando-se a "idade2"."""
"""A variável "message" utiliza a operação ternária para assumir um valor, com o a
condição de executar o "if" caso "check1" / "check2" sejam verdadeiros."""