num = int(input('Digite um número inteiro : '))
print('''Escolha uma das bases para conversão 
      [ 1 [ Converter para BINÁRIO
      [ 2 ] Converter para OCTAL 
      [ 3 ] Converter para HEXADECIMAL''')
opção = int(input('Sua opção : '))
if opção == 1:
    print('{} covertido para BINÁRIO é igual {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual {}'.format(num,oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual {}'.format(num, hex(num)[2:]))
else:
    print('\033[1;31m Opção invalida. Tente novamente\033[m! ')
