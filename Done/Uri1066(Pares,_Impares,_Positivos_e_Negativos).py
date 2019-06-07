x = 0
pares = 0
impares = 0
positivo = 0
negativo = 0
while x < 5:
    y = float(input())
    if y % 2 == 0:
        pares = pares + 1
    if y % 2 != 0:
        impares = impares + 1
    if y > 0:
        positivo = positivo + 1
    if y < 0:
        negativo = negativo + 1
    x = x + 1
print('{} valor(es) par(es)\n{} valor(es) impar(es)\n{} valor(es) positivo(s)\n{} valor(es) negativo(s)'
      .format(pares, impares, positivo, negativo), end='\n')
