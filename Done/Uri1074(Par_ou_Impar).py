N = int(input())
while N > 0:
    X = int(input())
    if X == 0:
        print('NULL', end='\n')
    elif X % 2 == 0 and X < 0:
        print('EVEN NEGATIVE', end='\n')
    elif X % 2 == 0 and X > 0:
        print('EVEN POSITIVE')
    elif X % 2 == 1 and X < 0:
        print('ODD NEGATIVE', end='\n')
    elif X % 2 == 1 and X > 0:
        print('ODD POSITIVE', end='\n')
    N = N - 1
