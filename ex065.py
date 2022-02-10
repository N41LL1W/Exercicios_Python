def Conta02():

    num = 0
    escolha = ''
    soma = quant = media = maior = menor = 0

    while escolha in 'Ss':
        num = int(input('Digite um número: '))
        soma += num
        quant += 1
        if quant == 1:
            maoir = menor = num
        else:
            if num > maior:
                maior = num
            if num < menor:
                menor = num
        escolha = str(input('Quer continuar? [ S / N ]')).upper().strip()[0]
        media = soma / quant
    print('Você digitou {} números e a média foi de {}'.format(quant, media))
    print('O maior valor foi {} e o menor foi {}'.format(maior, menor))

Conta02()