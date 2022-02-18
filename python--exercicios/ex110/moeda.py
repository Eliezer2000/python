def aumentar(preço, taxa, formatado=False):
    res = preço + (preço * taxa / 100)
    return res if formatado is False else moeda(res)



def diminuir(preço=0, taxa=0, formatado=False):
    res = preço - (preço * taxa / 100)
    return res if formatado is False else moeda(res)


def dobro(preço=0, formatado=False):
    res = preço * 2
    return res if formatado is False else moeda(res)


def metade(preço=0, formatado=False):
    res = preço / 2
    return res if formatado is False else moeda(res)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>5.2f}'.replace('.', ',')


def resumo(preço=0, taxaa=10, taxar= 5):
    print('=' * 30)
    print('Resumo do valor '.center(30))
    print('=' * 30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'O dobro do preço:\t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)} ')
    print(f'{taxaa}% de aumento \t\t{aumentar(preço, taxaa, True)}')
    print(f'{taxar}% de redução \t\t{diminuir(preço, taxar, True)}')

