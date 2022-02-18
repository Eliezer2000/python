#Escreva um programa que converta uma temperatura digitando um graus Celsius e converta para graus Fahrenheit
C = float(input('Informe a ttemperatura em Cº :'))
F = (9 * C / 5) + 32
print('A temperatura de \033[1;34m{}Cº\033[m  corresponde a \033[1;31m{}Fº\033[m'.format(C, F))


