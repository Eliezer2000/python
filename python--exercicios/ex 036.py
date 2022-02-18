#casa = float(input('Valor da casa : '))
#salário = float(input('Saláro do comprador : '))
#anos = int(input('Quantos anos de financiamento : '))
#prestação = casa / (anos * 12)
#minimo  = salário * 30 / 100
#print('Para pagar uma casa de \033[1;32m R${:.2f}\033[m em \033[1;32m{}  anos\033[m, a prestação será de \033[1;32m R$ {:.2f}\033[m'.format(casa, anos, prestação))
#if prestação <= minimo:
 #   print('O empréstimo pode ser \033[1;32mCONCEDIDO\033[m.')
#else:
   # print('Empréstimo \033[1;31mNEGADO\033[m!')

casa = float(input('Valor da casa R$ : '))
salário = float(input('Salário do comprador R$ : '))
anos = int(input('Quantos anos de financiamento  : '))
prestação = casa / (anos * 12)
minimo = salário * 30 / 100
print('Para pagar uma case de \033[1;32m R${:.2f}\033[m em \033[1;32m {} anos\033[m, a prestação será de \033[1;32m R${:.2f}\033[m'.format(casa, anos, prestação))
if prestação <= minimo:
    print('O emprestimo pode ser \033[1;32m CONCEDIDO\033[m.')
else:
    print('O empréstimo pode ser \033[1;31m NEGADO\033[m!')

