'''Metodo de Gauss-Sidel
NOME: Isabella                       RA:
NOME: Jean-Lucas Luquetti Silva      RA: 120443
NOME: Thamires Verri Ribeiro         RA: 140814
'''
# Coeficientes da matriz A (3x3) e B
A = [ 3, -1,  1,
      1,  5, -2, 
      2, -1,  4 ]

b = [3,
     4,
     5]

# Declaração do vetor resíduo
r = [0, 0, 0]

# Equações moldadas a partir das matrizes A e B
f1 = lambda x,y,z: (y - z + 3)/3
f2 = lambda x,y,z: (-x + 2*z + 4)/5
f3 = lambda x,y,z: (-2*x + y + 5)/4

# Valores iniciais de X1, X2, e X3
x0 = 0.5
y0 = 0
z0 = -0.5

# Tolerância e Iteração Máxima
e = 0.00000005
itermax = 10

# Declaração da condição e da iteração inicial
condition = True
iter = 0

# Estrutura do print
print(" k      normres       normrel")
print("---   -----------   -----------")

# Laço que executa iterações enquanto as condições de parada não forem atingidas
while condition:
    x1 = f1(x0,y0,z0)
    y1 = f2(x1,y0,z0)
    z1 = f3(x1,y1,z0)
    e1 = abs(x0-x1);
    e2 = abs(y0-y1);
    e3 = abs(z0-z1);

    # Vetores de X(k) e X(k+1) em módulo
    Xk  = [abs(x0), abs(y0), abs(z0)]
    Xk1 = [abs(x1), abs(y1), abs(z1)]

    # Cálculo do vetor resíduo em módulo
    r = [ abs(b[0] - (A[0]*x1 + A[1]*y1 + A[2]*z1)),
          abs(b[1] - (A[3]*x1 + A[4]*y1 + A[5]*z1)),
          abs(b[2] - (A[6]*x1 + A[7]*y1 + A[8]*z1)) ]
        
    # Norma-infinito do vetor resíduo e Erro relativo na norma-infinito
    normres = max(r)
    normrel = abs((max(Xk1) - max(Xk))/max(Xk1)) 
    if iter+1 < 10:
        print(f' {iter+1}    {normres:.5e}   {normrel:.5e}')
    else:
        print(f' {iter+1}   {normres:.5e}   {normrel:.5e}')

    # Atualização dos valores e do número de iterações
    iter += 1
    x0 = x1
    y0 = y1
    z0 = z1

    # Teste das condições de parada
    condition = e1>e and e2>e and e3>e and iter < itermax