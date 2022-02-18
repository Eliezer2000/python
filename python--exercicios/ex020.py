# O mesmo professor do desafio 19 quer sortear a ordem de apresentação do trabalho dos alunos.Faça um programa que leia o nome dos quatros alunos e mostre a ordem dos sorteados
import random

n1 = input('primeiro aluno : ')
n2 = input('Segundo  aluno : ')
n3 = input('Terceiro aluno : ')
n4 = input('Quarto aluno : ')
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem dos alunos será : ')
print(lista)
