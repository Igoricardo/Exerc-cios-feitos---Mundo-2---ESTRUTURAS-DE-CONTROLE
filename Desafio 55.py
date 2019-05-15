maior = 0
menor = 100*100
for x in range(1, 6):
   p = float(input('Informe o {}° peso: '.format(x)))
   if p > maior:
      maior = p
   if p < menor:
      menor = p
print('O maior peso informado foi:{}kg\nO menor peso informafo foi:{}kg'.format(maior, menor)) 
