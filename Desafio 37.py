n = int(input("""Informe um número,\033[1;34m(1)\033[m para converter para BINÁRIO,\033[1;35m(2)\033[m para OCTAL e \033[1;32m(3)\033[m para HEXADECIMAL:"""))
if n == 1:
    print('\033[1;34mVocê escolheu conversão BINÁRIA\033[m')
    x = int(input('Informe um número para converter:'))
    y = bin(x)
    print('O número informado foi \033[1;34m{}\033[m, convertido para BINÁRIO é \033[1;34m{}\033[m'.format(x, y[2:]))
elif n == 2:
    print('\033[1;35mVocê escolheu conversão OCTAL\033[m')
    x = int(input('Informe um número para converter:'))
    y = oct(x)
    print('O número informado foi \033[1;35m{}\033[m, convertido para OCTAL é \033[1;35m{}\033[m'.format(x, y[2:]))
elif n == 3:
    print('\033[1;32mVocê escolheu Conversão HEXADECIMAL\033[m')
    x = int(input('Informe um número para converter:'))
    y = hex(x)
    print('O número informado foi \033[1;32m{}\033[m, convertido em HEXADECIMAL é \033[1;32m{}\033[m'.format(x, y[2:]))
else:
    print('O número informado é invalido. Digite novamente')
