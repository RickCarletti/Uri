X, Y = map(int, input().split())
inicio = 1
while inicio < Y:
    rept = 1
    while rept <= X and inicio <= Y:
        if rept == X:
            print(inicio)
        else:
            print(inicio, end=' ')
        inicio = inicio + 1
        rept = rept + 1
