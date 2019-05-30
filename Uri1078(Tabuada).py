N = int(input())
X = 1
while X <= 10:
    result = N * X
    print('{} x {} = {}'.format(X, N, result), end='\n')
    X = X + 1
