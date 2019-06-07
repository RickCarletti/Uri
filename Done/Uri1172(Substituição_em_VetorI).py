X = []
for i in range(10):
    x = int(input())
    if x <= 1:
        X.append(1)
    else:
        X.append(x)
    print('X[{}] = {}'.format(i, X[i]))
