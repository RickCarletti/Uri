x = 1
y = 1
while x > 0 and y > 0:
    x, y = map(int, input().split())
    if x > 0 and y > 0:
        if x <= y:
            inicio = x
            fim = y
        else:
            inicio = y
            fim = x
        lista = []
        soma = 0
        while inicio <= fim:
            lista.append(inicio)
            soma = soma + inicio
            inicio = inicio + 1
        print(' '.join(map(str, lista)), 'Sum={}'.format(soma), end='\n')
# Uri não aceita "print(*lista, 'Sum={}'.format(soma), end='\n')", por conta do '*'. Motivo desconhecido
