n = s = quant = 0
while True:
    n = int(input('Digite um número : '))
    if n == 999:
        break
    s += n
    quant += 1
print(f'Você digitou {quant} e a soma entre eles é {s}')


s = quant = 0
while True:
    n = int(input('Digite um número e  999 para parar : '))
    if n == 999:
        break
    s += n
    quant += 1
print(f'Você digitou {quant} e a soma foi {s}')

