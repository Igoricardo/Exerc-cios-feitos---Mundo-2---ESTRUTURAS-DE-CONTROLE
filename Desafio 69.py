from pygame import mixer
mixer.init()
mixer.music.load('Audio exe 69.mp3')
mixer.music.play()
print('\n\033[1;4;34mFORMULÁRIO DE CADASTRO:\033[m')
opção = 'Ss'
maior_idade = homem = menor_20 = 0
while opção not in 'Nn':
    idade = int(input('\nInforme a Idade: '))
    if idade >= 18:
        maior_idade += 1
    sexo = str(input('Informe o sexo [M/F]: ')).strip().upper()
    while sexo not in 'MF':
        print('\033[1;31mInformação inválida, digite novamente!\033[m')
        sexo = str(input('Informe novamente o sexo [M = MASCULINO / F = FEMININO]: ')).strip().upper()
    if sexo in 'Mm':
        homem += 1
    elif sexo in 'Ff' and idade <= 19:
        menor_20 += 1
    opção = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    while opção not in 'SN':
        print('\033[1;31mInformação inválida, digite novamente!\033[m')
        opção = str(input('Ainda desejar continuar? [S = SIM/N = NÃO]: ')).strip().upper()
    if opção == 'Nn':
        break
print(f'''\n\033[1;4;33mRESULTADO DA PESQUISA:\033[m
\nPessoas acima de 18 anos são: {maior_idade}
Homens mencionados na pesquisa: {homem}
Mulheres abaixo de 20 anos: {menor_20}''')
