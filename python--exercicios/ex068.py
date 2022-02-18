from random import randint
while True:
    jogador = int(input('Digite um valor : '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    v = 0
    while tipo not in 'PpIi':
        tipo = str(input('Par ou ímpar ? ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador} total de {total} ', end=' ')
    print('Deu PAR ' if total % 2 == 0 else 'deu IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu !')
            v += 1
        else:
            print('Você perdeu !')
            break
    elif tipo == 'i':
        if total % 2 == 1:
            print('Você venceu !')
            v += 1
        else:
            print('você perdeu ! ')
            break
        print('Vamos jogar novamente !')
print(f'Game Over ! Você venceu {v} vezes. ')

from random import randint
while True:
    jogador = int(input('Digite um número : '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo =' '
    v = 0
    while tipo not in 'PpIi':
        tipo = str(input('Par ou Impar ? ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador} e o total foi {total}', end= ' ')
    print('Deu PAR' if total % 2 == 0 else 'Deu IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu ! ')
            v += 1
        else:
            print('Você perdeu !')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu !')
            v += 1
        else:
            print('Você perdeu !')
            break
    print('Vamos jogar novamente ...')
print(f'GANE OVER ! Você venceu {v} vezes.')

from random import randint
while True:
    jogador = int(input('Digite um número : '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    v = 0
    while tipo not in 'PpIi':
        tipo = str(input('Par ou ímpar ? ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu ! ')
            v += 1
        else:
            print('Você perdeu !')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu !')
            v += 1
            break
    print('Vamos jogar novamente ...')
print(f'GAME OVER ! Você venceu {v} vezes .')












































