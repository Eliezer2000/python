'''primeiro = int(input('Primeiro termo : '))
razão = int(input('Razão : '))
termo = primeiro
cont = 1
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end=' ')
        termo += razão
        cont += 1
    print('Pausa ')
    mais = int(input('Quantos termos você quer mostrar a mais ?'))
print('A progressão foi finalizada com {} termos contados. '.format(total))'''


'''primeiro = int(input('Primeiro Termo : '))
razão = int(input('Razão : '))
termo = primeiro
cont = 0
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end=' ')
        termo += razão
        cont += 1
    print('Pausa ')
    mais = int(input('Quantos termos você quer mostrar a mais ? '))
print('A progressão foi finalizada com {} termos contados. '.format(total))'''


primeiro = int(input('Primeiro termo : '))
razão = int(input('Razão : '))
termo = primeiro
cont = 0
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end=' ')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais ? '))
print('A progressão foi finalizada com {} termos contados '.format(total))
