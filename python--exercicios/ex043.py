peso = float(input('Digite seu peso : (KG) '))
altura = float(input('Digite sua altura (M) : '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc <= 18.5:
    print('você esta abaxo do peso normal . ')
elif 18.5 < imc <= 25:
    print('Você está com o peso NORMAL')
elif 25 < imc <= 30:
    print('Você está com SOBREPESO')
elif 30 < imc <= 40:
    print('Você está com OBESIDADE')
elif  imc >= 40:
    print('Você está com OBESIDADE MÓRBIDA')

peso = float(input('Digite seu peso : KG'))
altura = float(input('Digite seu peso : M '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é {:.1f}'.format(imc))
if imc <= 18.5:
    print('Você está abaixo do peso normal!')
elif 18.5 < imc <= 25:
    print('Você está com peso normal!')
elif 25 < imc <= 30:
    print('Você está com sobrepeso!')
elif 30 < imc <= 40:
    print('VocÊ está OBESO!')
elif imc >= 40:
    print('Você está com OBESIDADE MÓRBIDA')

