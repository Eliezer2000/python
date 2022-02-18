tot18 = totaldehomens = totaldemulher20 = 0
while True:
    print('Cadastre uma pessoa : ')
    print('=' * 30)
    idade = int(input('Idade : '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo : [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totaldehomens += 1
    if sexo == 'F' and idade < 20:
        totaldemulher20 += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar ? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos {tot18}')
print(f'E o total de Homens é {totaldehomens}')
print(f'Ao todo são {totaldemulher20} de mulheres  com menos de 20 anos.')
tot18 = toth = totm = 0
while True:
    idade = int(input('Idade : '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo : [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        toth += 1
    if sexo == 'F' and idade < 20:
        totm += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar ? ')).strip().upper()[0]
    if resp == 'N':
        break

print(f'Total de pessoas com mais de 18 anos {tot18}')
print(f'O total de homens é de {toth}')
print(f'O total de mulher maior que 20 é {totm} ')

tot18 = toth = totm = 0
while True:
    idade = int(input('Idade : '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo : [M/F] ')).strip().upper()[0]
        if idade >= 18:
            tot18 += 1
        if sexo == 'M':
            toth += 1
        if sexo == 'F' and idade < 20:
            totm += 1


    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar ? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'São {tot18} com mais de 18 anos. ')
print(f'São {toth} homens cadastrados.')
print(f'São {totm} mulheres com menos de 20 anos.')

tot18 = toth = totm = 0
while True:
    idade = int(input('Idade : '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo : [M/F] ')).strip().upper()[0]
        if idade >= 18:
            tot18 += 1
        if sexo == 'M':
            toth += 1
        if sexo == 'F' and idade < 20:
            totm += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar ? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'São ao todo {tot18} pessoas com mais de 18 anos.')
print(f'Foram {toth} homens cadastrados. ')
print(f'Ao todo são {totm} mulheres com menos de 20 anos.')




