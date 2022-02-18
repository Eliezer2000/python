'''ficha = list()
doc = dict()
gols = []
tot = 0
for c in range(0, 1):
    doc['Nome'] = str(input('Nome : '))
    doc['Partidas'] = int(input(f'Quantas partidas {doc["Nome"]} jogou ? '))
print(doc)

for c in range(0,doc["Partidas"]):
    Gols = int(input(f'Quantos gols na partida {c} : '))
    gols.append(Gols)
    doc['Gols'] = gols
    tot += Gols
    doc['Total'] = tot
ficha.append(doc.copy())
print(doc)

print('-='* 50)

for c in ficha:
    print(f'O campo nome tem o valor {c["Nome"]}')
    print(f'O campo Gols tem o valor {c["Gols"]}')
    print(f'O campo Total tem o valor {c["Total"]}')
print('-=' * 50)
g = doc["Gols"]
print(f'O jogador {c["Nome"]} jogou {c["Partidas"]} partidas.')
for c in range(0, c["Partidas"]):
    print(f'-> Na partida {c} ele fez  ')

print()'''


jogador = dict()
partidas = list()
jogador['Nome'] = str(input('Nome do jogador : '))
tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou ? '))
for c in range(0, tot):
    partidas.append(int(input(f'Quantos gols {jogador["Nome"]} fez na partida {c} : ')))
jogador['Gols'] = partidas[:]
jogador['Total'] = sum(partidas)
print('-='* 60)
print(jogador)
print('-='*60)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('=-'* 60)
print(f'O jogador {jogador["Nome"]} jogou {len(jogador["Gols"])} partidas. ')
for i, v in enumerate(jogador['Gols']):
    print(f'  => Na partida {i}, fez {v} gols. ')
print(f'Foi um total de {jogador["Total"]} gols. ')


























