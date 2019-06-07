p1 = list(map(float, input().split()))
p2 = list(map(float, input().split()))
x1 = p1[0]
y1 = p1[1]
x2 = p2[0]
y2 = p2[1]
Distancia = ((x2 - x1)**2 + (y2 - x1)**2) ** (1/2)
print('{:.4f}'.format(Distancia), end='\n')
