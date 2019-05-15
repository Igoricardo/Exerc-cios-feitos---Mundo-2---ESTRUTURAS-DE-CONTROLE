r = 1
c = 1
n = int(input('Informe um número a ser fatorado: '))
while c <= n:
    r *= c # É a mesma coisa que r = r * c
    c += 1 # É a mesma coisa que c = c + 1
print('O número a ser fatorado é {}! e o seu fatorial é {}.'.format(n, r))

'''
Este é modo mais simples de resolver este exxercício:
from math import factorial
n = int(input('Informe um número: ')
f = factorial(n)
print('O número informado foi {} e seu fatorial é {}'.format(n, f)
'''

