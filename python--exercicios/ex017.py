# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.Calcule e mostre o comprimento da hipotenusa.
import math
co = float(input('Digite o comprimento do cateto oposto : '))
ca = float(input('Digite o comprimento do cateto adjacente : '))
hi = math.hypot(co, ca)
print('\033[1;32m A hipotenusa vai medir\033[m  \033[1;36m{:.2f}\033[m'.format(hi))







