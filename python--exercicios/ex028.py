from random import randint
from time import sleep
computador = randint(0,5)    # Faz o computador ''Pensar''
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5, tente advinhar ! ')
print('-=-' *20)
jogador = int(input('Em que número eu pensei ? '))       # O jogador tenta advinhar
print('Processando...')
sleep(3)
if jogador == computador:
    print('Parabéns você conseguiu me vencer !')
else:
    print('GANHEI! Eu pensei no número {} e não no número {}'.format(computador,jogador))






