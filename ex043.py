def Imc():
    peso = float(input('Qual o seu peso? '))
    altura = float(input('Qual a sua altura? '))
    imc = peso / ((altura / 100) ** 2)
    print('Sua altura de {}cm e seu peso de {}kg'.format(altura, peso))
    print('Da um IMC de {:.2f}.'.format(imc))

    if imc <= 18.5:
        print('Você está ABAIXO DO PESO.')
    elif imc > 18.5 and imc <= 25:
        print('Você está no PESO IDEAL.')
    elif imc > 25 and imc <= 30:
        print('Você está com SOBREPESO.')
    elif imc > 30 and imc <= 40:
        print('Você está com OBESIDADE.')
    else:
        print('Você está com OBESIDADE MORBIDA.')


Imc()
