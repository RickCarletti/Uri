def soma_impar(inicio, fim):
    somaim = 0
    inicio = inicio + 1
    while inicio < fim:
        if inicio % 2 != 0:
            somaim = somaim + inicio
        inicio = inicio + 1
    return somaim


N = int(input())
while N > 0:
    W = list(map(int, input().split()))
    X = W[0]
    Y = W[1]
    if X >= Y:
        inicio = Y
        fim = X
    else:
        inicio = X
        fim = Y
    somaim = soma_impar(inicio, fim)
    print('{}'.format(somaim), end='\n')
    N = N - 1
