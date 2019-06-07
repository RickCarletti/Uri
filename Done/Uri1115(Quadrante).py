X = 1
Y = 1
while X != 0 and Y != 0:
    W = list(map(int, input().split()))
    X = W[0]
    Y = W[1]
    if X > 0 and Y > 0:
        print('primeiro', end='\n')
    elif X < 0 and Y > 0:
        print('segundo', end='\n')
    elif X < 0 and Y < 0:
        print('terceiro', end='\n')
    elif X > 0 and Y < 0:
        print('quarto', end='\n')
