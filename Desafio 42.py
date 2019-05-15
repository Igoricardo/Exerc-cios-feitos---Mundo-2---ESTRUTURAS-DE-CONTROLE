x = float(input('Informe o 1° lado do triângulo:'))
y = float(input('Informe o 2° lado do triângulo:'))
z = float(input('Informe o 3° lado do triângulo:'))
if (y-z) < x < y + z and (x-z) < y < x + z and (x-y) < z < x + y:
    print('É possível montar um triângulo com as medidas informadas.')
    if x == y and x == z and y == z:
        print('Este triângulo é \033[1;7;4;35mEQUILÁTERO\033[m.')
    elif x != y and x != z and y != z:
        print('Este triângulo é \033[1;4;7;33mESCALENO\033[m.')
    elif x == y or x == z or y == z:
        print('Este triângulo é \033[1;7;4;34mISÓSCELES\033[m.')
else:
    print('Não é possível montar um triângulo com as medidas informadas.')

