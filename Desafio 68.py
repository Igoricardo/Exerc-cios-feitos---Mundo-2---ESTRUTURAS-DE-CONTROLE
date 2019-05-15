from random import randint
from pygame import mixer
mixer.init()
mixer.music.load('Audio exe 68.mp3')
mixer.music.play()
print('JOGO DO PAR OU ÍMPAR')
contador = 0
while True:
    n = int(input('\nInforme um N°: '))
    computador = randint(0, 10)
    s = n + computador
    resposta = str(input('PAR OU ÍMPAR? [P/I]: ')).strip().upper()
    if resposta not in 'PI':
        print('Digito Inválido, Informe P = PAR e I = ÍMPAR.')
        break
    if s % 2 == 0:
        print(f'O N° do JOGADOR: {n} / N° do COMPUTADOR: {computador}. O TOTAL da soma: {s}. DEU PAR!')
        if resposta == 'P':
            print('VOCÊ VENCEU! PORQUE ESCOLHEU PAR.')
            contador += 1
        else:
            print(f'VOCÊ PERDEU! PORQUE ESCOLHEU ÍMPAR.')
            break
    else:
        print(f'O N° do JOGADOR: {n} / N° do COMPUTADOR: {computador}. O TOTAL da soma: {s}. DEU ÍMPAR!')
        if resposta == 'I':
            print('VOCÊ VENCEU! PORQUE ESCOLHEU ÍMPAR.')
            contador += 1
        else:
            print(f'VOCÊ PERDEU! PORQUE ESCOLHEU PAR.')
            break
print(f'\nGAME OVER! Você conseguiu vencer o computador {contador} vez(es)')
