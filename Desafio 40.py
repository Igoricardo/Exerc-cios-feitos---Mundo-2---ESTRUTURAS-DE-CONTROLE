n1 = float(input('Informe a 1° nota:'))
n2 = float(input('Informe a 2° nota:'))
m = (n1 + n2) / 2
if m < 5:
    print('Sua média é {:.1f}, você esta \033[1;31mREPROVADO!\033[m'.format(m))
elif m >= 5 and m <= 6.9:
    print('Sua média é {:.1f}, você esta de \033[1;33mEXAME!\033[m'.format(m))
else:
    print('Sua média é {:.1f}, você esta \033[1;32mAPROVADO!\033[m'.format(m))
    