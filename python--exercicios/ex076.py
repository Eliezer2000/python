listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.28,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livros', 34.08,)
print('-=' * 30)
print(f'{"Listagem de preços":^40}')
print('=-' * 30)
for pos in range(0,len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem [pos]:.<30}', end=' ')
    else:
        print(f'R${listagem[pos]:>6.2f}')
print('-' * 40)

