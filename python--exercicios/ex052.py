num = int(input('Digite um número : '))
tot = 0
for c in range(1, num +1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end=' ')
print('O número {} foi dividido {} vezes'.format(num, tot))
if tot == 2:
    print('E por isso ele é PRIMO')
   else:
       print('Por isso ele não é PRIMO')



num = int(input('Digite um número : '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('O número {} foi divisivel {} vezes'.format(num, tot))
if tot == 2:
    print('Por isso ele é PRIMO')
else:
    print('Por isso ele não é primo')



num = int(input('Digite um número : '))
tot = 0
for c in range(1, num + 1):
    print('{}'.format(c), end=' ')
    if num % c == 0:
        print('\033[34m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('O número {} foi dividido em {} vezes '.format(num, tot))
if tot == 2:
    print('Por isso ele é PRIMO')
else:
    print('Ele não é primo')





