def leiaint(msg):
    while True:
        try:
            n = int(input('Digite um número inteiro : '))
        except (ValueError, TypeError):
            print('\033[0;31m Erro! Digite um número inteiro.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31m O usuário preferiu não digitar esse número\033[m')
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input('Digite um número real : '))
        except (ValueError, TypeError):
            print(f'\033[0;31m Erro! Digite um número real\033[m')
        except KeyboardInterrupt:
            print('\033[0;31m O usuário preferiu não digitar esse número\033[m')
            return 0
        else:
            return n


n1 = leiaint('Digite um número : ')
n2 = leiafloat('Digite um número real : ')
print(f'O valor inteiro digitado foi {n1} e o número real foi {n2} ')


