#crie um programa que leia dois numeros e mostre a soma entre eles
#n1= int(input('Digite um valor:'))
#n2= int(input('Digite outro valor:'))
#s= n1+n2
#print('A soma entre {} e {} é {}'.format(n1, n2, s))

n1 = int(input('Digite um valor : '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
print('A soma entre {}{}{} e {}{}{} é {}{}{}'.format('\033[34m',n1,'\033[m', '\033[34m',n2,'\033[m', '\033[32m',s,'\033[m'))
