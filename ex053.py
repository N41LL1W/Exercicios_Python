def Inversao():

    frase = str(input('Digite alguma coisa: ')).strip().upper()
    palavras = frase.split()
    junto = ''.join(palavras)
    inverso = ''

    for letra in range(len(junto) -1, -1, -1):
        inverso += junto[letra]
    if inverso == junto:
        print('Temos um palíndromo!')
    else:
        print('A frase digita não é um palídromo!')


Inversao()