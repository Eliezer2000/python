# Um professor quer sortear um de seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, tendo o nome dos alunos e escrevendo na tela o nome do escolhido
import random
n1 = input('Primeiro aluno : ')
n2 = input('Segundo  aluno : ')
n3 = input('Terceiro aluno : ')
n4 = input('Quarto   aluno : ')
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('\033[4;34m O aluno escolido foi\033[m \033[4;32m{}\033[m'.format(escolhido))

