resp = 'S'
soma = quant = média = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número : '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar [S/N] ? ')).upper().strip()[0]
média = soma / quant
print('Você digitou {} números e a média foi {}'.format(quant, média))
print('O maior valor foi {}  e o  menor valor foi {}'.format(maior, menor))



resp = 'S'
média = soma = quant = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número : '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
                menor = num
    resp = str(input('Quer continuar : [S/N] : ')).upper().strip()[0]
média = soma / quant
print('Você digitou {} números e a média foi {} '.format(quant, média))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))



resp = 'S'
soma = média = quant = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número : '))
    quant += 1
    soma += num
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar [S/N] ? ')).upper().strip()[0]
média = soma / quant
print('você digitou {} números e a média é {} '.format(quant, média))
print('O maior foi {} e o menor foi {}'.format(maior, menor))




resp = 'S'
soma = quant = média = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número : '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar [S/N] ? ')).upper().strip()[0]
média = soma / quant
print('Você digitou {} números e a média é {} '.format(quant, quant))
print('O maior foi {}  e o  menor foi {}'.format(maior, menor))





resp = 'S'
soma = quant = média = 0
while resp in 'Ss':
    num = int(input('Digite um número : '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar [S/N] ? '))
média = soma / quant
print('Você digitou {} números e a média é de {}'.format(quant, média))
print('O maior é {} e o menor é {}'.format(maior, menor))























