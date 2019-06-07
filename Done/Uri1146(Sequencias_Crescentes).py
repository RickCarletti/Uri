X = 1
while X != 0:
    X = int(input())
    cont = 1
    while cont <= X:
        if cont < X:
            print(cont, end=' ')
        else:
            print(cont, end='\n')
        cont = cont + 1
