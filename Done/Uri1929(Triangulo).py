bla = list(map(int, input().split()))
bla.sort()
if abs(bla[0]-bla[2]) < bla[1] < bla[0] + bla[2] or abs(bla[1] - bla[3]) < bla[2] < bla[1] + bla[3]:
    print('S')
else:
    print('N')
