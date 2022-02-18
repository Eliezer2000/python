print('   Banco   ' )
valor = int(input('Que valor você quer sacar ? '))
total = valor
céd = 50
totalcéd = 0
while True:
    if total >= céd:
        total -= céd
        totalcéd += 1
    else:
        if totalcéd > 0:
            print(f'Total de {totalcéd} cédulas  de R${céd}')
            if céd == 50:
                céd = 20
            elif céd == 20:
                céd = 10
            elif céd == 10:
                céd = 1
            totalcéd = 0
            if total == 0:
                break
print('Volte sempre ao Banco')

valor = int(input('Qual valor você vai sacar ? '))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} células de R$ {céd}')
            if céd == 50:
                céd = 20
            elif céd == 20:
                céd = 10
            elif céd == 10:
                céd = 1
            totcéd = 0
            if total == 0:
                break
print('Fim do programa')


valor = int(input('Qual valor você vai sacar ? '))
total = valor
céd = 200
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R$ {céd}')
            if céd == 200:
                céd = 100
            elif céd == 100:
                céd = 50
            elif céd == 50:
                céd = 20
            elif céd == 20:
                céd = 10
            elif céd == 10:
                céd = 5
            elif céd == 5:
                céd = 2
            elif céd == 2:
                céd = 1
            totcéd = 0
            if total == 0:
                break


valor = int(input('Qual valor você vai sacar ?  '))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} de R$ {céd}')
            if céd == 50:
                céd = 20
            elif céd == 20:
                céd = 10
            elif céd == 10:
                céd = 1
            totcéd = 0
            if total == 0:
                break
print('Obrigado Volte sempre')'''

for c in range(0, 10, 3):
    print(c)
    















