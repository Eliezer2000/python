def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31m Erro! Digite um número inteiro.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31m O usuário preferiu não digitar esse número\033[m')
            return 0
        else:
            return n


def linha(tam = 42):
    return '=' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaint('Sua opção : ')
    return opc


