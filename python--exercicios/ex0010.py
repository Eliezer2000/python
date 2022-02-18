# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
#x = float(input('O valor que você possui:  R$'))
#dolar = x / 5.37
#euros = x / 6.44
#libras = x / 7.46
#print('Com R${:.2f} você poderá comprar US${:.2f} de doláres '.format(x, dolar))
#print('Com R${:.2f} você podera comprar {:.2f} Euros'.format(x, euros))
#print('Com R${:.2f} você podera comprar {:.2f} Libras'.format(x, libras))



x = float(input('O valor que você possui:  R$'))
dolar = x / 5.37
euros = x / 6.44
libras = x / 7.46
print('Com \033[32m R${:.2F}\033[m você poderá comprar \033[32m US${:.2f}\033[m  de doláres'.format(x, dolar))
print('Com \033[32m R${:.2f}\033[m você poderá comprar \033[32m{:.2f}\033[m  Euros'.format(x, euros))
print('Com \033[32m R${:.2f}\033[m você poderá comprar \033[32m{:.2f}\033[m Libras'.format(x, libras))




