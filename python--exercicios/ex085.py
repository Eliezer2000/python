'''dados = [[], []]
valor = 0
for c in range(0,8):
    valor = int(input(f'Digite o {c} valor : '))
    if valor % 2 == 0:
        dados[0].append(valor)
    elif valor % 2 == 1:
        dados[1].append(valor)
print('-='* 40)
dados[0].sort()
dados[1].sort()
print(dados)
print(f'Os números pares registrados foram {dados[0]}')
print(f'Os números ímpares registrados foram {dados[1]}')'''

dados = [[], []]
valor = 0
for c in range(0,7):
    valor = int(input(f'Digite o {c} valor : '))
    if valor % 2 == 0:
        dados[0].append(valor)
    elif valor % 2 == 1:
        dados[1].append(valor)
dados[0].sort()
dados[1].sort()
print(dados)
print(f'Os valores Pares {dados[0]}')
print(f'Os valores ímpares são {dados[1]}')















