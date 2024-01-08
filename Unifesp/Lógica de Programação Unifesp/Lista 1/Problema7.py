fulano = float(1.50) #Jean-Lucas Luquetti Silva / RA: 120443
ciclano = float(1.10)
anos = int(-1)
while (fulano >= ciclano): #Laço que aumenta as alturas de ambos até que ciclano passe fulano, com um contador de anos.
    fulano = fulano + 0.02
    ciclano = ciclano + 0.03
    anos = anos+1
print(anos)