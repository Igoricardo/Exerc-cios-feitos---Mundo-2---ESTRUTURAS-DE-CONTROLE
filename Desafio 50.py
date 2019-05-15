s = 0
c = 0
for x in range(0, 6):
    n = int(input('Informe um valor inteiro:'))
    if n % 2 == 0:
        s = s + n
        c = c + 1
print('\nVocê informou {} números pares!\nA soma de todos os valores PARES informados é {:2}'.format(c, s))
