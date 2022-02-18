nome = input('Digite seu nome : ')
print('\033[1;34m Seu nome em Maiúsculo é\033[m \033[1;32m{}\033[m :'.format(nome.upper()))
print('\033[1;34m Seu nome em Minúsculo é\033[m \033[1;32m{}\033[m :'.format(nome.lower()))
print('\033[1;36m O seu nome tem ao todo\033[m  \033[1;32m{}\033[m \033[1;36mletras\033[m:'.format(len(nome)))
print('\033[1;33m Seu nome tem ao todo\033[m \033[1;32m{}\033[m \033[1;33mletras\033[m '.format(len(nome) - nome.count(' ')))
#print('O seu primeiro nome tem {} letras : '.format(nome.find(' ')))
separa= nome.split()
print('\033[1;33m o primeiro nome é\033[m \033[1;33m{}\033[m \033[1;33m e tem\033[m \033[1;32m{}\033[m \033[1;33mletras\033[m '.format(separa[0], len(separa[0])))














