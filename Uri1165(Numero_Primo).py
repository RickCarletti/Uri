N = int(input())
for N in range(N):
    X = int(input())
    divisor = X
    cont = 0
    for X in range(1, X+1):
        if divisor % X == 0:
            cont = cont + 1
    if cont == 2:
        print('{} eh primo'.format(divisor), end='\n')
    else:
        print('{} nao eh primo'.format(divisor), end='\n')
