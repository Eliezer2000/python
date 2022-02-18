# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno, e tângente desse ãngulo
import math
ângulo = float(input('Digite o ãngulo que você deseja : '))
seno = math.sin(math.radians(ângulo))
print('\033[1;35mO ângulo de\033[m  \033[1;32m{}\033[m \033[1;35m tem o Seno de\033[m \033[1;32m[{:.2f}\033[m '.format(ângulo, seno))
cosseno = math.cos(math.radians(ângulo))
print('\033[4;33m O cosseno de\033[m  \033[4;32m{}\033[m \033[4;33m é\033[m  \033[4;32m{:.2f}\033[m '.format(ângulo, cosseno))
tangente = math.tan(math.radians(ângulo))
print('\033[7;40m A tangente de\033[m  \033[7;32m{}\033[m \033[7;40m é\033[m \033[7;32m{:.2f}\033[m'.format(ângulo, tangente))




