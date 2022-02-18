num = list()
while True:
    num.append(int(input('Digite um valor : ')))

    resp = str(input('Quer continuar ? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Você digitou {len(num)} elementos')
num.sort(reverse=True)
print(f'Os valores em ordem decrescente são {num}')
if 5 in num:
    print('O valor 5 faz parte desta lista.')
else:
    print('O valor 5 não faz parte desta lista.')
print('Programa encerrado!')



