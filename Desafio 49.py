n = int(input('Informe qual a tabuada que deseja consultar:'))
for m in range(0, 11):
    print('{} x {:2} = {:2}'.format(n, m, n*m))
