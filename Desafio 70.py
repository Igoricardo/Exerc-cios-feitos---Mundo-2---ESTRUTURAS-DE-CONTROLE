s = contador_preço = menor_preço = c_menor_preço = 0
opção = 's'
nome_mp = ''
while opção in 's':
    nome = str(input('\nInforme o nome do produto: '))
    preço = float(input('Qual o preço? R$'))
    c_menor_preço += 1
    s += preço
    if preço > 1000:
        contador_preço += 1
    if c_menor_preço == 1 or preço < menor_preço:
        menor_preço = preço
        nome_mp = nome
    opção = str(input('Deseja continuar? [S/N]: ')).strip().lower()
    while opção not in 'sn':
        opção = str(input('Opção inválida! Desaja continuar? [S/N]: '))
    if opção == 'Nn':
        break
print(f'''
Total gasto na compra: R$\033[1;32m{s}\033[m
Quantos produtos custam mais de R$1000,00? \033[1;32m{contador_preço}\033[m produto(s)
Qual é o nome do produto mais barato? \033[1;32m{nome_mp}\033[m''')