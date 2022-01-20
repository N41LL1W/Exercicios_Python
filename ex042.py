def Triangulo():
    print('-=-' * 20)
    print('Analizador de Triâmgulos')
    print('-=-' * 20)
    s1 = float(input('Primeiro segmento: '))
    s2 = float(input('Segundo segmento: '))
    s3 = float(input('Terceiro segmento: '))
    if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s2 + s1:
        print('Esses segmentos de retas formam um triangulo!')
        if s1 == s2 and s1 == s3 and s2 == s3:
            print('E esse triangulo é EQUILÁTERO.')
        elif s1 == s2 or s1 == s3 or s2 == s3:
            print('E esse triangulo é ISÓCELES.')
        elif s1 != s2 and s1 != s3 and s2 != s3:
            print('E esse triangulo é ESCALENO.')
    else:
        print('Esses segmentos de retas NÃO formam um triangulo!')


Triangulo()
