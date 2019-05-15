n = int(input('Informe o 1° termo:'))
r = int(input('Informe a razão:'))
d = n + 9 * r
for x in range(n, d+r, r):
    print(x, end=' > ')
print('\nO 1° termo é {} e a razão é {}'.format(n, r))