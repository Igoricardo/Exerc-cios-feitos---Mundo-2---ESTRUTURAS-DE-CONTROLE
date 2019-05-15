from math import pow
p = float(input('Informe seu peso:'))
a = float(input('Informe sua altura:'))
imc = p / pow(a, 2)
if imc < 18.5:
    print('Seu IMC é {:.1f}. Você esta abaixo do peso!'.format(imc))
elif imc >= 18.5 and imc <= 25:
    print('Seu IMC é {:.1f}. Você esta no seu peso ideal!'.format(imc))
elif imc > 25 and imc < 30:
    print('Seu IMC é {:.1f}. Você esta com sobrepeso!'.format(imc))
elif imc > 30 and imc < 40:
    print('Seu IMC é {:.1f}. Você esta obeso!'.format(imc))
else:
    print('Seu IMC é {:.1f}. Você está com obesidade mórbida!'.format(imc))