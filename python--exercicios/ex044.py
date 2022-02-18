print('{:=^40}'.format('Loja do fulano'))
preço = float(input('Valor das compras : '))
print(''' FORMAS DE PAGAMENTO \n [ 1 ] á vista dinheiro / cheque \n [ 2 ] á vista cartão \n [ 3 ] 2x no cartão \n [ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual a opção : '))
if  opção == 1:
    desconto = preço - (preço * 10 / 100)
    print('A sua compra de R$ {:.2f} á vista no dinheiro / cheque será de R$ {:.2f} com 10% de desconto'.format(preço, desconto))
elif opção == 2:
    desconto2 = preço - (preço * 5 / 100)
    print('A sua compra de R$ {:.2f} á vista no cartão será de R$ {:.2f} com 5% de desconto'.format(preço, desconto2))
elif opção == 3:
    print('Em até 2x no cartão o preço será formal de R$ {:.2f}'.format(preço))
elif opção == 4:
    juros = preço + (preço * 20 / 100)
    totalparc = int(input('Quantos de parcelas ? '))
    parcela = juros / totalparc
    print('Sua compra será parcelada em {}x de R$ {:.2f} COM JUROS '.format(totalparc, parcela))
    print('Com 3x ou mais no cartão o valor será de {:.2f} com 20% de juros'.format(juros))
else:
    total = 0
    print('\033[1;31m Opção invalida de pagamento tente novamente!\033[m ' )



