from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento : '))
idade = atual - nasc
if idade <= 9:
    print('O atleta tem {} anos. \n Classificação \033[1;33m Mirim\033[m'.format(idade))
elif 14 >= idade >= 9:
    print('O atleta tem {} anos. \n Classificação \033[1;33m Infantil\033[m'.format(idade))
elif 19 >= idade >= 14:
    print('O atleta tem {} anos. \n Classificação \033[1;33m jÚNIOR\033[m '.format(idade))
elif 25 >= idade >= 19:
    print('O atleta tem {} anos. \n Classificação \033[1;33m Sênior\033[m'.format(idade))
else:
    print('O atleta tem {} anos. \n Classificação \033[1;33m Master\033[m'.format(idade))


