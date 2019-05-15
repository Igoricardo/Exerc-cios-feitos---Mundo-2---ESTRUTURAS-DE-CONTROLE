n = int(input('Informe um número:'))
t = 0
for x in range(1, n+1):
    if n % x == 0:
        print('\033[1;33m', end=' ')
        t += 1 # É o mesmo que t = t + 1, pois esta maneira de escrever (t += 1) é a forma simplificada
    else:
        print('\33[1;31m', end=' ')
    print('{}'.format(x), end=' ')
print('\033[m\nO número {} foi divisível {} vezes'.format(n, t))
if t == 2:
    print('Este número é PRIMO')
else:
    print('Este número NÃO É PRIMO')
