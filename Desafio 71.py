print('\033[1;4;32mSIMULAÇÃO DE CAIXA ELETRÔNICO\033[m')
saque = int(input('\nInforme o valor que deseja sacar: R$ '))
valor = saque
nota = 50
cont = 0
print('Você sacou R$ \033[1;32m{:.2f}\033[m que forem destribuidos pelo caixa da seguinte forma:'.format(saque))
while True:
    if valor >= nota:
        valor -= nota
        cont += 1
    else:
        print
        print('Cédulas: \033[1;33m{}\033[m / Valor sacado: R$ \033[1;34m{:.2f}\033[m'.format(cont, nota))
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        cont = 0
        if valor == 0:
            break
            