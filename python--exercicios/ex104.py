'''def leiaint(n):
    while True:
        n = str(input('Digite um número : '))
        if n.isnumeric():
            n = int(n)
            break
        else:
            print('ERRO! Digite um número inteiro válido. ')
    return n


#programa principal
n = leiaint('Digite um número : ')
print(f'Você acabou de digitar o número {n}')'''


def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok :
            break
    return valor


n = leiaint('Digite um número  : ')
print(f'Você acabou de digitar o número {n} ')















