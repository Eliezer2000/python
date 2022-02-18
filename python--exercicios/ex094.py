pessoa = dict()
galera = list()
soma = média = 0
while True:
    pessoa.clear()
    pessoa['Nome'] = str(input('Nome : '))
    while True:
        pessoa['Sexo'] = str(input('Sexo : [M/F] : ')).upper()[0]
        if pessoa['Sexo'] in 'MF':
            break
        print('ERRO! Por favor digite apenas M ou F ')
    pessoa['idade'] = int(input('Idade : '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar ? [S/N] : ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S OU N. ')
    if resp == 'N':
        break
print('-=-'*60)
print(f'A) Ao todo foram cadastradas {len(galera)} pessoas.')
média = soma / len(galera)
print(f'B) A média de idade é de {média:5.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end=' ')
for p in galera:
    if p['Sexo'] in 'Ff':
        print(f'{p["Nome"]} ',end=' ')
print()
print('Lista das pessoas que estão acima da média ',end=' ')
for p in galera:
    if p['idade'] >= média:
        print('     ')
        for k, v in p.items():
            print(f'{k} = {v}; ',end=' ')
        print()
print('>>> ENCERRADO! <<<')



























