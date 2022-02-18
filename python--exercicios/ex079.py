'''números = list()
while True:
    n = int(input('Digite um valor : '))
    if n not in números:
        números.append(n)
        print('Valor adicionado  com sucesso!')
    else:
        print('Valor duplicado. Não vou adcionar...')

    r = str(input('Quer continuar [S/N] ? ')).strip().upper()[0]
    if r in 'N':
        break
print('=-' * 30)
números.sort()
print(f'Você digitou os valores {números}')



números = list()
while True:
    n = int(input('Digite um  número : '))
    if n not in números:
        números.append(n)
        print('Número adicionado com sucesso!')
    else:
        print('Valor duplicado.Não vou adicionar.')
    r = str(input('Quer continuar [S/N] : ')).strip().upper()[0]
    if r in 'N':
        break
print('->' * 80)
números.sort()
print(f'Você digitou os valores {números}')'''

números = list()
while True:
    n = int(input('Digite um valor : '))
    if n not in números:
        números.append(n)
        print('Valor adicionado!')
    else:
        print('Valor duplicado! Não vou adicionar.')
    r = str(input('Quer continuar [S/N] ? ')).strip().upper()[0]
    if r == 'N':
        break
números.sort()
print(f'OS números  digitados foram {números}')
























