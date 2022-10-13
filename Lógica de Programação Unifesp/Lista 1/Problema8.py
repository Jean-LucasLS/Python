r = float(input()) #Jean-Lucas Luquetti Silva / RA: 120443
v = float()
while (r <= 20): #laço que calcula o valor do volume (com pi = 3.1415) utilizando-se a fórmula dada e imprimindo no formato float com 4 casas após a vírgula
    v = (4/3)*3.1415*(r**3)
    print('{:.4f}'.format(v))
    r = r+0.5