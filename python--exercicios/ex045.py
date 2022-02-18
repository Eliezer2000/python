from random import randint
from time import sleep
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('''Suas opções : 
[ 0 ] pedra
[ 1 ] papel
[ 2 ] tesoura''')
jogador = int(input('Qual é a sua jogada ? '))
print('JO')
sleep(1)
print('KE')
sleep(1)
print('PÔ !!!')
print('-=' * 11)
print('Computador jogou {} '.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0:     #Computador jogou pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE!')
    elif jogador == 2:
        print('COMPUTADOR VENCE!')
    else:
        print('Jogada inválida!')


elif computador == 1:  #Computador jogou papel
    if jogador == 0:
        print('COMPUTADOR VENCE!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCE!')
    else:
        print('Jogada inválida!')

elif computador == 2:  #Computador jogou tesoura
    if jogador == 0:
        print('JOGADOR VENCE!')
    elif jogador == 1:
        print('COMPUTADOR VENCE!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('Jogada inválida!')


