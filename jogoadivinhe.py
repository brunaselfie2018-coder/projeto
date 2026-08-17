#jogo da adinhaçâo desafio 58
from random import randint
comp = randint(0, 10)
print('Sou seu computador, acabei de pensar em um número entre 0 e 10')
print('consegue adivinhar?')
Acertou = False
palpite = 0
while not Acertou:
    jogador = int(input('Escolhe um número pra você adivinhar:'))
    palpite += 1
    if jogador == comp:
        acertou = True
    else:
        if jogador < comp:
            print('Mais tente mais uma vez!')
        elif jogador > comp:
            print('Menos, tente mais uma vez!')
print(f'Acertou com {palpite} tentetivas, Parabéns!')
