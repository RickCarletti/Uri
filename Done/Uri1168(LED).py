listaled = {'1': 2, '2': 5, '3': 5, '4': 4, '5': 5, '6': 6, '7': 3, '8': 7, '9': 6, '0': 6}
N = int(input())
for i in range(N):
    V = str(input())
    qnts = 0
    for j in V:
        qnts += listaled[j]
    print(qnts, 'leds')
