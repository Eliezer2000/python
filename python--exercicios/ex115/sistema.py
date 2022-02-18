from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'Cursoemvideo.txt'

if arquivoExiste(arq):
    print('Arquivo encontrado com sucesso!')
else:
    print('Arquivo não encontrado!')
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas','Cadastrar novas pessoas', 'Sair do sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa
        cabeçalho('Novo cadastro')
        nome = str(input('Nome : '))
        idade = leiaint('Idade : ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        cabeçalho('ERRO! Digite uma opção válida!')
    sleep(2)







