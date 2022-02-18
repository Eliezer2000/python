# Faça um programa que leia a largura e a altura de uma parede em metros. Calcule a sua área e a quantidade da tinta necessária para pintá-la , sabendo que cada litro de tinta pinta uma área de 2m2
larg = float(input('Largura da parede:'))
alt = float(input('Altura da parede:'))
Área = larg * alt
print('Sua parede tem a dimensão de {} x {} e a Área é de {}m².'.format(larg, alt, Área))
tinta = Área / 2
print('Para pintar essa parede você precisará de {}l de tintas. '.format(tinta))
