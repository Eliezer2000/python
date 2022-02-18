tabela = ('Atletico-MG', 'Palmeiras', 'Fortaleza', 'Bragantino', 'Flamengo',
          'Atletico=PR', 'Ceará SC', 'Santos', 'Atletico-GO', 'Bahia',
          'Internacional', 'Corinthians', 'Fluminense', 'Juventude', 'Sport Recife',
          'São Paulo', 'América-MG', 'Cuiaba', 'Grêmio', 'Chapecoense')
print('=' * 400)
print(f'Lista de Times do Brasileirão : {tabela}')
print('=' * 400)

print('Os 5 primeiros são : ',tabela[0:5])
print('=' * 400)

print('Os últimos 4  colocados são : ',tabela[-4:])
print('=' * 400)

print(f'Times em ordem alfabética :',sorted(tabela))
print('=' * 400)

print(f'A Chapecoense está na {tabela.index("Chapecoense") + 1 }º posição')
print('=' * 400)




