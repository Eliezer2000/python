'''from time import sleep
n1 = int(input('Primeiro valor : '))
n2 = int(input('Segundo valor : '))
opção = 0
while opção != 5:
    print(' [ 1 ] Somar.\n [ 2 ] Multiplicar\n [ 3 ] Maior\n [ 4 ] Novos números\n [ 5 ] Sair do programa ')
    opção = int(input('Qual é a sua opção ? '))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))
    elif opção == 2:
        multiplicação = n1 * n2
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, multiplicação))
    elif opção == 3:
        if n1 > n2:
            print('Entre {} e {} o maior é {}'.format(n1, n2, n1))
        if n2 > n1:
            print('Entre {} e {} o maior é {}'.format(n1, n2 , n2))
        else:
            print('Os números {} e {} são iguais.'.format(n1, n2))
    elif opção == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro número : '))
        n2 = int(input('Segundo número : '))
    elif opção == 5:
        print('Finalizando . . . ')
        print('-=-' * 20)
        print('Fim do programa! Volte sempre!')
        print('-=-' * 20)
        sleep(2)
    else:
        print('Opção inválida.Digite novamente.')'''
from time import sleep
n1 = int(input('Primeiro número : '))
n2 = int(input('Segundo número : '))
opção = 0
while opção != 5:
    sleep(2)
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos Números
    [ 5 ] Sair do programa''')
    opção = int(input('Qual a sua opção : '))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))
    elif opção == 2:
        produto = n1 * n2
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, produto))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior é {}'.format(n1, n2, maior))
    elif opção == 4:
        print('Informe os números novamente.')
        n1 = int(input('Primeiro número : '))
        n2 = int(input('Segundo número : '))
    elif opção == 5:
        print('Finalizando . . . ')
        sleep(1)
        print('-=' * 20)
        print('Programa finalizado. Volte sempre!')














