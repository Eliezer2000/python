#faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações ossiveis sobre ele
a= input('Digite algo:')
print('O tipo primitivo desse valor é:',type(a))
print('Só tem espaços?',a.isspace())
print('É um numero?',a.isnumeric())
print('É alfabético?',a.isalpha())
print('É alfanumérico?',a.isalnum())
print('Está em maiúsculo?',a.isupper())
print('Está em minúsculo?',a.islower())
print('Está capitalizado?',a.capitalize())



