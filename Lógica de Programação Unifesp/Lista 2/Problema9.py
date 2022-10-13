n = int(input()) #Jean-Lucas Luquetti Silva / RA: 120443
ultimo = 1
penultimo = 1
if (n==0): #Caso "n" seja 0, o print será 0
    print("0")
elif (n==1): #Caso "n" seja 1, o print será 1
    print("1")
else :
    aux=2
    while aux <= n:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        aux = aux + 1
    print(termo)