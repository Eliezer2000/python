'''print('=' * 30)
print('  LOJA SUPER BARATÃO   ')
print('=' * 30)
tot = totmil = cont = menor = 0
barato = ' '
while True:
    produto = str(input('Nome do produto : '))
    preço = float(input('Preço : R$  '))
    cont += 1
    tot += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto

    resp = ' '
    while resp not in 'S/N':
        resp = str(input('Quer continuar ? [S/N]  ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total do gasto da compra  foi R$ {tot:.2f} reais. ')
print(f'Temos {totmil} produtos que custam mais de 1000 reais.')
print(f'O produto mais barato foi {barato} custa R$ {menor} reais.')

total = totmil = menor = cont =  0
barato = ' '
while True:
    produto = str(input('Produto : '))
    preço = float(input('Preço : R$ '))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto

    resp = '  '
    while resp not in 'SN':
        resp = str(input('Quer continuar ? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total da compra foi R$ {total:.2f} Reais.')
print(f'Temos {totmil} produtos que custam acima de R$ 1000 reais. ')
print(f'O produto mais barato foi {barato} e o preço foi R$ {menor} Reais.')

total = totmil = cont = menor =  0
barato = ' '
while True:
    produto = str(input('Produto : '))
    preço = int(input('Preço : '))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        preço < menor
        menor = preço
        barato = produto


    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar ? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total da compra foi de R$ {total}')
print(f'Temos {totmil} produtos acima de 1000 reais.')
print(f'O  produto mais barato foi {barato} e custa  {menor}')
total =  totmil = cont= menor = 0
barato = ' '
while True:
    produto = str(input('Produto : '))
    preço = int(input('Preço : '))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        preço < menor
        menor = preço
        barato = produto


    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar ? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total da compra foi de R$ {total} reais.')
print(f'Temos {totmil} de produtos acima de R$ 1000 reais.')
print(f'O produto mais barato foi {barato} e o menor preço {menor}')'''

total = totmil = cont = menor =  0
barato = ' '
while True:
    produto = str(input('Produto : '))
    preço = float(input('Preço : R$ '))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        preço < menor
        menor = preço
        barato = produto

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar ? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total gasto na compra foi R$ {total} reais.')
print(f'Temos {totmil} produtos que custam mais de R$ 1000 reais')
print(f'O produto mais barato foi {barato} e o preço é R$ {menor}')


















