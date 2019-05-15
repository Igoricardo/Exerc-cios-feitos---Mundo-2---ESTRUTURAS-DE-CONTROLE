#-----------------Aplicação de comparação e analise de dados--------------------

nv = '' # Variavel para receber o nome do homem mais velho
si = 0  # Variavel para receber a soma de todas as idade informadas
m = 0   # Variavel para receber a média de idade das pessoas do grupo
menori = 0  # Variavel para receber o total de mulheres com menos de 20 anos
maiori = 0  # Variavel para verificar qual homem é o mais velho

for x in range(1, 5):
    print('-'*30)
    nome = str(input('\nNOME: ')).strip().title()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F]: '))
    si += idade
    if sexo in 'Mm':
        nv = nome
        maiori = idade
        if idade > maiori:
            nv = nome
            maiori = idade
    if sexo in 'Ff' and idade < 20:
        f = 1
        menori += f
m = si / 4
print('''O homem mais velho do grupo se chama {} com {} anos.
No grupo ha {} mulher(es) com menos de 20 anos
E a média de idade das pessoas deste grupo é {}'''.format(nv, maiori, menori, m))
