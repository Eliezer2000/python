temp = list()
princ = list()
maior = menor = 0
while True:
    temp.append(str(input('Nome : ')))
    temp.append(float(input('Peso : ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]

    princ.append(temp[:])
    temp.clear()

    resp = str(input('Quer continuar ? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
print(princ)
print(f'Ao todo se cadastraram {len(princ)} pessoas.')
print(f'O maior peso é {maior}Kg  de ',end=' ')
for p in princ:
    if p[1] == maior:
        print(f'{p[0]}',end=' ')
print(f'\nO menor peso é {menor}',end=' ')
for p in princ:
    if p[1] == menor:
        print(f'{p[0]}',end=' ')



