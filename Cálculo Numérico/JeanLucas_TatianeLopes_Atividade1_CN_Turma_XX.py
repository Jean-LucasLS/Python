from math import *

'''f = Função f(x)
df = Derivada da função f(x)
x0 = Ponto inicial
eps: Tolerância
itmax = Iteração máxima
'''
f = lambda x: x*e**-x
df = lambda x: (e**-x)*(1-x)
x0 = 2.0
eps = 10**-8
itmax = 20

def Newton(f, df, x0, eps, itmax):
    iteration = 1
    k = x0
    for i in range(1, itmax+1):
        if df(k) != 0 and f(k) != 0:
            xk = k - (f(k) / df(k))
            stepk = xk - k
            if stepk < 0:
                stepk = stepk * -1
            if iteration < 10:
                print(f' {iteration}', end='   ')
            else:
                print(f' {iteration}', end='  ')
            print(f' {xk:.5e}', end='   ')
            print(f'{f(xk):.5e}', end='   ')
            print(f'{stepk:.5e}')
            k = xk
            iteration = i+1
        if f(xk) <= eps:
            break

print(' k        xk          f(xk)         stepk   ')
print('----  ------------  ------------  -----------')
Newton(f, df, x0, eps, itmax)