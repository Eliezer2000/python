frase = str(input('Digie uma frase : ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
print('Você digitou a frase {}'.format(junto))
inverso = ''
for letra in range(len(junto) - 1, - 1, - 1):
   inverso += junto[letra]
if inverso == junto:
    print('Temos um Palindromo')
else:
    print('A frase digitada não é um palindro !')


frase = str(input('Digite uma frase : ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palindromo')
else:
    print('A frase digitada não é um palindro')
    

frase = str(input('Digite uma frase : ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
    if inverso == junto:
        print('Temos um palindromo')
    else:
        print('A frase diditada não é um palindromo ')









