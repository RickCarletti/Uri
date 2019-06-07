N = int(input()) * 2
X = 0
while N > 1:
    X = X + 1
    print('{} {} {}'.format(X, X**2, X**3))
    print('{} {} {}'.format(X, X**2 + 1, X**3 + 1))
    N = N - 2
