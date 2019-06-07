N = int(input())
while N > 0:
    X = list(map(float, input().split()))
    result = (X[0]*2 + X[1]*3 + X[2]*5)/10
    print('{:.1f}'.format(result), end='\n')
    N = N - 1
