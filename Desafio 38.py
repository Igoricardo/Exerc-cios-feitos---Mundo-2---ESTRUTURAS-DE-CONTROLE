a = int(input('Informe o 1° número:'))
b = int(input('Informe o 2° número:'))
if a > b:
    print('O 1° número é maior que o 2° ')
elif b > a:
    print('O 2° número é maior que o 1°')
elif a == b:
    print('{} e {} são números iguais!'.format(a, b))
