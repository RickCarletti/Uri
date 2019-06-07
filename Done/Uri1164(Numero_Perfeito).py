N = int(input())
for N in range(N):
    X = int(input())
    soma = 0
    x = X
    for X in range(1, X+1):
        if x % X == 0:
            soma = soma + X
    if soma == 2*x:
        print('{} eh perfeito'.format(X), end='\n')
    else:
        print('{} nao eh perfeito'.format(X), end='\n')
