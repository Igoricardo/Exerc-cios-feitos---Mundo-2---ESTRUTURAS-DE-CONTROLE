print('PROGRESSÃO ARITMÉTICA V3.0')
x = int(int(input('\nInforme o começo da PA: ')))
y = int(input('Informe a razão: '))
c = 1
t = x
novo_termo = 10
total = 0
while novo_termo != 0:
    total += novo_termo
    while c <= total:
        print('{}'.format(t), end=' >')
        t += y
        c += 1
    print('...')
    novo_termo = int(input('Quantos termos ainda deseja ver?'))
print('PA encerrada com {} termos.'.format(total))

