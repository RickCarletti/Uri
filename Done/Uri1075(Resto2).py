N = int(input())
X = 1
while X < 10000:
    if X % N == 2:
        print(X, end='\n')
    X = X + 1
