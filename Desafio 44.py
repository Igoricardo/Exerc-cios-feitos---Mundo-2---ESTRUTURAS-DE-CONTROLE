vp = float(input('Informe o valor do produto: R$'))
fp = int(input('''Abaixo estão as formas de pagamento:
    [1] À vista com Dinheiro / Cheque
    [2] À vista no Cartão
    [3] Até 2x no Cartão
    [4] 3x ou mais no Cartão
    Informe a forma de pagamento:'''))

if fp == 1:
    nvp = vp - (vp * 10 / 100)
    print('O valor do produto era R${:.2f}, com desconto de 10% você pagará R${:.2f}'.format(vp, nvp))

elif fp == 2:
    nvp = vp - (vp * 5 / 100)
    print('O valor do produto era R${:.2f}, com desconto de 5% você pagará R${:.2f}'.format(vp, nvp))

elif fp == 3:
    p = int(input('Parcele em até 2x:'))
    x = vp / p
    print('Você pagará R${:.2f} em {}x no cartão.'.format(x, p))
    print('O valor do produto era R${:.2f}, não há desconto, você pagará o mesmo valor'.format(vp))

elif fp == 4:
    p = int(input('Em quantas parcelas?'))
    nvp = vp + (vp * 20 / 100)
    x = nvp / p
    print('Você paragará R${:.2f} em {}x no cartão.'.format(x, p))
    print('O valor do produto era R${:.2f}, você pagará juros de 20%, desta forma o valor a pagar é R${:.2f}'.format(vp, nvp))

else:
    print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE.')
