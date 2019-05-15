from datetime import date
ano = int(input('Informe o ano em que você nasceu:'))
idade = date.today().year - ano
if idade <= 9:
    print('Idade: {} anos, Nasceu em: {}, pertece a categoria MIRIM.'.format(idade, ano))
elif idade >= 10 and idade <= 14:
    print('Idade: {} anos, Nasceu em: {}, pertence a categoria INFANTIL.'.format(idade, ano))
elif idade >= 11 and idade <= 19:
    print('Idade: {} anos, Nasceu em: {}, pertence a categoria JUNIOR.'.format(idade, ano))
elif idade >= 20 and idade <= 25:
    print('Idade: {} anos, Nasceu em: {}, pertence a categoria SÊNIOR.'.format(idade, ano))
else:
    print('Idade: {} anos, Nasceu em: {}, pertence a categoria MASTER.'.format(idade, ano))

