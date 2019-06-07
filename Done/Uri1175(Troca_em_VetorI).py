N = []
for i in range(20):
    N.append(int(input()))
N.reverse()
for i in range(20):
    print('N[{}] = {}'.format(i, N[i]))
