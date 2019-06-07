def soma_impar(inicio, fim):
    somaim = 0
    inicio = inicio + 1
    while inicio < fim:
        if inicio%2 != 0:
            somaim = somaim + inicio
        inicio = inicio + 1
    return somaim


X = int(input())
Y = int(input())
if X >= Y:
    inicio = Y
    fim = X
else:
    inicio = X
    fim = Y
somaim = soma_impar(inicio, fim)
print('{}'.format(somaim), end='\n')
