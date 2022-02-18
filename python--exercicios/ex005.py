# Faça um programa que leia um número inteiro e mostre na tela o seu suceesor e seu antecessor
#n1 = int(input('Digite um némero'))
#su = n1 - 1
#s = n1 + 1
#print('O antecessor de {} e {} e o sucessor é {}'.format(n1, su, s))

print('Digite um número para saber o antecessor e o sucessor. ')
n1 = int(input('Digite um número : '))
su = n1 - 1
s = n1 +1
print('O antecessor de {}{}{} é {}{}{} e o suceesor é {}{}{}'.format('\033[32m',n1,'\033[m', '\033[31m',su,'\033[m', '\033[34m', s, '\033[m'))
