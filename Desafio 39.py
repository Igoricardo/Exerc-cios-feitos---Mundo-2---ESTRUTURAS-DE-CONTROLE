from datetime import date
n = int(input('Informe o ano de seu nascimento:'))
idade = date.today().year - n
if idade == 18:
    print('Você tem {} anos, é hora de se alistar ao serviço militar.'.format(idade))
elif idade < 18:
    print('Você tem {} anos, falta {} anos para você se alistar ao serviço militar'.format(idade, idade-18))
else:
    print('Você tem {} anos e já passou {} anos do tempo de alistamento'.format(idade, idade-18))
