N = int(input())
while N > 0:
    X, Y = map(int, input().split())
    if Y == 0:
        print('divisao impossivel', end='\n')
    else:
        print('{:.1f}'.format(X/Y), end='\n')
    N = N - 1
