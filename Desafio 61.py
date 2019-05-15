print('PROGRESSÃO ARITIMÉTICA')
n = int(input('\nInforme um número: '))
r = int(input('Informe a razão: '))
c = 1
t = n
while c <= 10:
    print('{} > '.format(t), end='')
    t += r
    c += 1
print('FIM DA PA')