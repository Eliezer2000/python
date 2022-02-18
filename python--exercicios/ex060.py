from math import factorial
n = int(input('Digie um número para obter o factorial dele : '))
f = factorial(n)
print('O factorial de {} é {}'.format(n,  f))

n = int(input('Digite um número para obter o seu factorial  : '))
c = n
f = 1
print('Calculando = {}! '.format(n), end=' ')
while c > 0:
    print('{} '.format(c), end=' ')
    print('x' if c > 1 else '=', end=' ')
    f *= c
    c -= 1
print('{}'.format(f))

n = int(input('Digite um número : '))
c = n
f = 1
print('Calculando = {}! '.format(n), end=' ')
for c in range(n, 0, - 1):
    print('{} '.format(c), end=' ')
    print('x' if c > 1 else '=', end=' ')
    f *= c
    c -= 1
print('{}'.format(f))

