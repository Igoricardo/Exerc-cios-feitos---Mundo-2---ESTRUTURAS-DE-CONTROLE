f = str(input('Digite uma frase: ')).strip().upper()
i = f[::-1]
for x in range(0, 1):
   if f == i:
     print('Esta frase é um palíndromo!')
   else:
     print('Esta frase não é um palíndromo!')
print ('Você digitou: {} \ne a frase invertida ficou desta forma: {}'.format(f, i))