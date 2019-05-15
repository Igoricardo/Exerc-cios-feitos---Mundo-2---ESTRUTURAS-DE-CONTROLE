sexo = str(input('Informe o sexo [\033[1;34mM = Masculino\033[m / \033[1;35mF = Feminino\033[m]: ')).strip().upper()
while sexo not in 'MF':
    print('\033[1;31mOpção inválida!\033[m Por favor insira a informação correta.')
    sexo = str(input('Informe o sexo [M/F]: ')).strip().upper()
if sexo == 'M':
    print('Informação correta, o sexo informado foi \033[1;34mMASCULINO!\033[m')
else:
    print('Informação correta, o sexo informado foi \033[1;35mFEMININO!\033[m')

