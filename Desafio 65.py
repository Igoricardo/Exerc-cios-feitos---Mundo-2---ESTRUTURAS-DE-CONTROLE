s = cont = m = 0
opção = 'sS'
while opção in 'sS':
    n = int(input('\nInforme um N°: '))
    s += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    opção = str(input('\033[1;31mDeseja continuar? [S/N]: \033[m')).strip().upper()
    if opção == 'N':
        print('\033[1;33mVocê deseja encerrar o programa. Até logo!\033[m')
m = s / cont
print('''\nN° informados: {}
Soma enrte os N°: {}
Média entre os N°: {:.2f}
Maior N°: {}
Menor N°: {}'''.format(cont, s, m, maior, menor))
