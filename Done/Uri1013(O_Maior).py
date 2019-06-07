n = list(map(int, input().split()))
A = n[0]
B = n[1]
C = n[2]
MaiorAB = (A + B + abs(A - B))/2
MaiorABC = (MaiorAB + C + abs(MaiorAB - C))/2
print('{:.0f} eh o maior'.format(MaiorABC), end='\n')
