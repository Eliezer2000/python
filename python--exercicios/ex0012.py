#Faça um algoritima que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preço = float(input('Digite o preço do produto : R$'))
novo = preço - (preço * 5 / 100)
print('O preço de \033[1;32mR${:.2f}\033[m com \033[4;33m5%\033[m de desconto é \033[1;32mR${:.2f}\033[m'.format(preço, novo))



