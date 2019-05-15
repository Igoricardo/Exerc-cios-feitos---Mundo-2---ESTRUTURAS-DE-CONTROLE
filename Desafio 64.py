n = 0
s = 0
cont = 0
print('\033[4;7;35mTRATAMENTO DE VALORES V1.0\033[m\n')
print('PARA ENCERRAR O PROGRAMA INFORME O N° \033[1;31m[999]!\033[m ')
while n <= 998:
        n = int(input('Informe um N°: '))
        s += n
        r = s - 999
        cont += 1
        c = cont - 1
print('''Software encerrado!
Foram informados {} números e a soma de todos os números informados é \033[1;4;31m{}\033[m'''.format(c, r))

