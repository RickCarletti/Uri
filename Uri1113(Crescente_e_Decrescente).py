X = 1
Y = 0
while X != Y:
    W = list(map(int, input().split()))
    X = W[0]
    Y = W[1]
    if X > Y:
        print('Decrescente', end='\n')
    elif X < Y:
        print('Crescente', end='\n')
