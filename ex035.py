print('-=-' * 20)
print('Analizador de Triâmgulos')
print('-=-' * 20)
s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s2 + s1:
    print('Esses segmentos de retas formam um triangulo!')
else:
    print('Esses segmentos de retas NÃO formam um triangulo!')
