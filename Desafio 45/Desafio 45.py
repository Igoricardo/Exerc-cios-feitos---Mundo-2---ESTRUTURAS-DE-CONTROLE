from random import choice
from time import sleep
from pygame import mixer

mixer.init()
mixer.music.load('Desafio 45.mp3')
mixer.music.play()

print('\033[1;31m=-\033[m'*30)
n = int(input('''Vamos jogar Jokenpô:
    [0] PEDRA
    [1] PAPEL
    [2] TESOURA
    Digite uma das 3 opções acima:'''))

item = ('PEDRA', 'PAPEL', 'TESOURA')

print('\033[1;31m=-\033[m'*30)

j1 = ['PEDRA', 'PAPEL', 'TESOURA']
j = choice(j1)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')

print('\033[1;31m=-\033[m'*30)

if n == 0 and j == 'TESOURA' or n == 1 and j == 'PEDRA' or n == 2 and j == 'PAPEL':
    print('O computador jogou {}, você jogou {}. VOCÊ GANHOOU!'.format(j, item[n]))
elif n == 0 and j == 'PAPEL' or n == 1 and j == 'TESOURA' or n == 2 and j == 'PEDRA':
    print('O computador jogou {}, você jogou {}. VOCÊ PERDEU!'.format(j, item[n]))
elif n == 0 and j == 'PEDRA' or n == 1 and j == 'PAPEL' or n == 2 and j == 'TESOURA':
    print('O computador jogou {}, você jogou {}. EMPATE!'.format(j, item[n]))
else:
    print('JOGADA INVÁLIDA')
