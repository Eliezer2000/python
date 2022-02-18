num = int(input('Digite um número : '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('\033[1;35m Analisando o número\033[m \033[1;32m{}\033[m '.format(num))
print('\033[1;35m Unidade:\033[m \033[1;32m{}\033[m'.format(u))
print('\033[1;35m Dezena:\033[m \033[1;32m{}\033[m '.format(d))
print('\033[1;35m Centena:\033[m \033[1;32m{}\033[m'.format(c))
print('\033[1;35m Milhar:\033[m \033[1;32m{}\033[m '.format(m))




