s = contador = 0
while True:
    n = int(input('Digite um N°: '))
    if n == 999:
        break
    s += n
    contador += 1
print(f'Foram informados {contador} números e a soma entre eles resultou no valor {s}')