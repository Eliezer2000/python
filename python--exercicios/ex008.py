# Escreva um programa que leia um valor em metros e exiba convertido em centímetros e milimetros
metros = int(input('Digite uma medida para converter:'))
cm = metros * 100
mm = metros * 1000
print('A medida \033[32m{}\033[m convertida para centimetros é \033[1;33m{}\033[mcm e para milimetros \033[4;34m{}\033[m mm'.format(metros, cm, mm))




