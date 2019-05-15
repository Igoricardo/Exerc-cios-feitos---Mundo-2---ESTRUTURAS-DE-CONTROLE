x = 0
y = 1
cont = 3
w = 0
print('\n\033[1;4;33mSEQUÊNCIA DE FIBONACCI\033[m')
n = int(input('\nInforme o número de termos que deseja ver: '))
print('\n0 + {0} = \033[1;32m{0}\033[m\n0 + {1} = \033[1;32m{1}\033[m'.format(x, y))
while cont <= n:
    print('{} + {}'.format(x, y), end='')
    w = x + y
    x = y
    y = w
    cont += 1
    print(' = \033[1;32m{}\033[m'.format(w))
print('\nFim do programa!')
