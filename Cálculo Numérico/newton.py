from math import *

'''x0 = Ponto inicial
eps: Tolerância Epsolon
'''
f = lambda x: x**2
df = lambda x: 2*x

def Newton(f, df, x0, eps, itmax):
    L = range(1,itmax+1)
    iteration = 1
    k = x0
    for i in L:
        if df(k) != 0: 
            xk = k - f(k) / df(k)
            stepk = xk - k
            if stepk < 0:
                stepk = stepk * -1
            print(f' {iteration}    {xk:.5f}     {f(xk):.5f}     {stepk:.5f}   ')
            k = xk
            iteration = i+1
        else:
            print("Houve divisão por zero, com f'(k) = 0")
            return
        if abs(stepk) <= eps:
            break
print(' k       xk        f(xk)       stepk   ')
print('---- ----------- ----------- -----------')
L = Newton(f, df, 1.5, 0.0001, 5)