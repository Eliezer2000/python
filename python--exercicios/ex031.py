distãncia = float(input('Qual é a distânca da sua viagem ? '))
print('Você está prestes a começar uma vagem de {} Km! '.format(distãncia))
if distãncia <= 200:
    preço = distãncia * 0.50
else:
    preço = distãncia * 0.45
print('E o preço da sua passagem será de {:.2f}'.format(preço))

