from time import sleep
def contador(i, f, p):
    print(f'Contagem de {i} até  {f} de {p} em {p}')
    sleep(1)
    if p  < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ',end=' ')
            sleep(0.5)
            cont += p
        print('Fim')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ',end=' ')
            sleep(0.5)
            cont -= p
        print('Fim!')


#programa principal
contador(1, 10, 1)
contador(10, 2, 1)
print('Agora é sua vez de personalizar a contagem : ')
ini = int(input('inicio  :  '))
fim = int(input('Fim     :  '))
pas = int(input('Passo   :  '))
contador(ini, fim, pas)