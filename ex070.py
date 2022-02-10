def Compra():
    seguir = barato = ''
    tot = caro = menor = cont = 0
    print('-'*30)
    print('LOJA SUPER BARATÃO')
    print('-' * 30)
    while True:
        nome = str(input('Nome do produto: '))
        preco = float(input('Preço: R$ '))
        cont += 1
        tot += preco
        if preco > 1000:
            caro += preco
        if cont == 1 or preco < menor:
            menor = preco
            barato = nome
        seguir = ' '
        while seguir not in 'SN':
            seguir = str(input('Deseja continuar? [S/N] ')).strip().upper() [0]
        if seguir == 'N':
            break
    print(f'Gasto total é {tot:.2F}')
    print(f'Gasto total com produtos acima R$ 1000 é de R$ {caro:.2F}')
    print(f'O produto mais barato foi {barato} que custa R$ {menor:.2f}')

Compra()