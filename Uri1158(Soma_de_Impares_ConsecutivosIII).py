N = int(input())
for N in range(N):
    X, Y = map(int, input().split())
    soma = 0
    for Y in range(Y):
        if X % 2 == 1:
            soma = soma + X
        else:
            X = X + 1
            soma = soma + X
        X = X + 2
    print(soma)
