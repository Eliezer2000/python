n1 = float(input('Primeira nota : '))
n2 = float(input('Segunda nota  : '))
média = (n1 + n2) / 2
if média >= 7.0:
    print('Tirando {} e {} a média do aluno é {} \n Você está \033[1;32m aprovado\033[m! '.format(n1, n2, média))
elif média >= 5 and média < 6.9:   # 6.9 > média >= 5
    print('Tirando {} e {} a média do aluno é {} \n Você está de \033[1;33m recuperação\033[m! '.format(n1, n2, média))
elif média < 5:
    print('Tirando {} e {} a média do aluno é {} \n Você está \033[1;31m REPROVADO\033[m!'.format(n1, n2, média))



