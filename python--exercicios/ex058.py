'''from random import randint
computador = randint(0, 10)
print('Sou seu computador ! Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi ? ')
acertou = False
pálpite = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite ? '))
    pálpite += 1
    if jogador == computador:
        acertou = True
    elif jogador < computador:
        print('Mais . . .  tente mais uma vez!')
    elif jogador > computador:
        print('Menos . . . Tente mais uma vez!')
print('ACERTOU com {} pálpites.'.format(pálpite))'''

'''from random import randint
computador = randint(0, 10)
print('Sou seu computador acabei de pensar em um número entre 0 e 10. ')
print('Será que você consegue adivinhar qual foi ? ')
acertou = False
pálpites = 0
while not acertou:
    jogador = int(input('Qual é o seu pálpite ? '))
    pálpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais ... Tente mais uma vez ')
        elif jogador > computador:
            print('Menos ... Tente mais uma vez')
print('Acertou {} pálpites'.format(pálpites))'''


from random import randint
computador = randint(0, 10)
print('Sou seu computador acabei de pensar em um número  entre 0 e 10.')
print('Será que você consegue adivnhar ? ')
acertou = False
pálpite = 0
while not acertou:
    jogador = int(input('Qual é seu pálpite :'))
    pálpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais')
        elif jogador > computador:
            print('Menos')
print('ACERTOU com {} pálpites  !'.format(pálpite))




