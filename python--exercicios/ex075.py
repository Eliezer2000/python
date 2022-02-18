num = (int(input('Digite um número : ')),
    int(input('Digite outro número : ')),
    int(input('Digite mais um número : ')),
    int(input('Digite o último número : ')))
print('=' * 50)
print(f'Você digitou os valores {num}')
print('=' * 50)
print(f'O número 9  apareceu {num.count(9)} vezes.')
print('=' * 50)
if 3 in num:
    print(f'O primeiro valor 3 foi digitado na {num.index(3)+1} posição.')
else:
    print('O valor 3 não foi digitado')
print('=' * 50)
print('Oa valores Pares são ', end=' ')
for n  in num:
    if n % 2 == 0:
        print(f'{n}', end=' ')









num = (int(input('Digite um número : ')),
      int(input('Digite um número : ')),
      int(input('Digite um número : ')),
      int(input('Digite um número : ')))
print('=-=' * 100)
print(f'Você digitou {num}')
print('=-=' * 100)
print(f'O número 9 apareceu {num.count(9)} vezes ')
print('=-=' * 100)
if 3 in num:
      print(f'O 3 foi digitado primeiro na {num.index(3) + 1} posição')
else:
      print('O número 3 não foi digitado.')
print('=-=' * 100)
print('Os valores Pares são ', end=' ')
for n in num:
      if n % 2 == 0:
            print(f'{n}', end=' ')















