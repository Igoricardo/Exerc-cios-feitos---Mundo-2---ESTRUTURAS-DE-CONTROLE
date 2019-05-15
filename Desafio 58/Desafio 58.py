from random import randint
from time import sleep
from pygame import mixer
x = False
total1 = 0
total2 = 0
print('JOGO DA ADIVINHAÇÃO DE NÚMEROS INTEIROS - ACERTE O NÚMERO QUE O COMPUTADOR ESTÁ PENSANDO!!!')
mixer.init()
mixer.music.load('musica.mp3')
mixer.music.play()
while not x:
    print('*'*100)
    n = int(input('\nInforme um número inteiro de 0 a 10: '))
    c = randint(0, 10)
    sleep(1)
    print('\033[1;32mLoading...\033[m')
    sleep(1)
    if 0 < n > 10:
        print('Número informado inválido! Por favor informe número de 0 a 10.')
        total1 += 1
    elif n != c:
        print('\033[1;31mVOCÊ ERROU! QUE PENA!\033[m \nN° do Computador: \033[1;33m{}\033[m / N° do Jogador: \033[1;33m{}\033[m'.format(c, n))
        total2 += 1
    else:
        print('\033[1;34mVOCÊ ACERTOU! PARABÉNS!\033[m \nN° do Computador: \033[1;33m{}\033[m / N° do Jogador: \033[1;33m{}\033[m'.format(c, n))
        x = True
        total2 += 1
print('\033[1;34m-\033[m'*100)
print('Para vencer foram necessários \033[1;7;31m{}\033[m palpites e \033[1;7;31m{}\033[m números inválidos!'.format(total2, total1))
