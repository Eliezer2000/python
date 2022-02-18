from random import randint
from time import sleep
lista = list()
jogos = list()
cont = 0
tot = 1
quant = int(input('Quantos jogos você quer fazer ? '))
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        lista.append(num)
        cont += 1
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f'===== Sorteando jogos =====')
for i, l in enumerate(jogos):
    print(f'Jogo {i+1} {l}')
    sleep(1)
print(f'Boa sorte')














