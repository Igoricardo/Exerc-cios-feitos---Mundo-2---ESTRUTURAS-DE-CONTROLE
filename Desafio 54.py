from datetime import date
totalMaior = 0
totalMenor = 0
totalAnciao = 0
for x in range(1, 8):
    nome = str(input('Informe o nome completo: ')).strip().title()
    ano = int(input('Informe o ano de nascimento: '))
    anoAtual = date.today().year
    idade = anoAtual - ano
    if idade >= 18 and idade <= 122:
        totalMaior += 1
        print('''
        O nome da pessoa é {}.
        A idade da pessoa é {} anos, portanto é maior de idade pois já passou {} anos da idade mínima.'''.format(nome, idade, idade-18))
        print('\033[1;31m-=\033[m'*55)
    elif idade >122:
        totalAnciao += 1
        print('''
        Está pessoa é a pessoa mais velha registrada na história mundial com {} anos!'''.format(idade))
        print('\033[1;31m-=\033[m'*55)
    else:
        totalMenor += 1
        print('''
        O nome da pessoa é {}.
        A idade da pessoa é {} anos, portanto é menor de idade pois faltam {} anos para atingir a maioridade'''.format(nome, idade, 18-idade))
        print('\033[1;31m-=\033[m'*55)
print('O número de pessoas maiores de idade: {} \nE menores de idade informados: {} \nPessoas que superam a maior idade de uma pessoa viva já registrada {}'.format(totalMaior, totalMenor, totalAnciao))
