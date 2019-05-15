s = 0
c = 0
for x in range (1, 500+1, 2):
    if x % 3 == 0:
        s = s + x
        c = c + 1
print('\nEsse é o resultado da soma de todos os valores impares: {} somando todos os {} números divisiveis por 3.'.format(s, c))
