X = float(input())
N = [X]
for i in range(100):
    print('N[{}] = {:.4f}'.format(i, N[i]))
    N.append(N[i]/2)
