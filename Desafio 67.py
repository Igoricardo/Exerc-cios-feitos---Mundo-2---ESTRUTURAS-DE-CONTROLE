while True:
    n = int(input('\nInforme qual tabuada deseja visualizar: '))
    contador = 1
    if n <= 0:
        break
    while contador <= 10:
        print(f'{n} x {contador} = {n*contador:2}')
        contador += 1
print('Programa encerrado, até logo!')






