matriz = [[0, 0, 0], [0, 0, 0,], [0, 0, 0,]]
pares = 0
maior = scol = 0
s = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor na posição [{l}, {c}] :  '))
        if matriz[l][c] % 2 == 0:
            s += matriz[l][c]
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]',end=' ')
    print()
print(f'A soma de todos os valores pares digitados foi {s}')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma da coluna 2 é {scol}')
for c in range(0, 3):
    if c == 0:
        maior = matriz[l][c]
    elif matriz[l][c] > maior:
        maior = matriz[l][c]
print(f'O maior valor da segunda linha é {maior}')

