lista = list()
listapares = list()
listaimpares = list()
while True:
    num = int(input('Digite um número : '))
    lista.append(num)
    resp = str(input('Quer continuar ? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
print('=' * 40)
print(f'A lista completa é {lista}')              #minha solução
for num in lista:
    if num % 2 == 0:
        listapares.append(num)

    elif num % 2 == 1:
        listaimpares.append(num)

print(f'lista de Pares {listapares}', end=' ')

print(f'\nLista de Ímpares {listaimpares}', end=' ')



num = list()
pares = list()
ímpares = list()
while True:
    num.append(int(input('Digite um número : ')))
    resp = str(input('Quer continuar ? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
for i, v in enumerate(num):                  #Solução do professor
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        ímpares.append(v)
print('-=' * 40)
print(f'A lista completa é {num}')
print(f'A lista de Pares {pares}')
print(f'A lista de ímpares {ímpares}')
