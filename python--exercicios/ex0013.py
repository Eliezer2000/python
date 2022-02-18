# Faça um algorítmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento:
salário = float(input('Digite o valor do seu salário : R$'))
aumento = salário + (salário * 15 / 100)
print('Um funcionário que ganhava R$\033[4:34m{:.2f}\033[m com \033[1;35m15%\033[m de aumento irá ganhar \033[4:32mR${:.2f}\033[m'.format(salário, aumento))

