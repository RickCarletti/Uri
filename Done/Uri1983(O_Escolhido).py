n = int(input())
nota = 7.9
listanota = []
for i in range(n):
    listanota.extend(list(map(float, input().split())))
    if listanota[-1] > nota:
        nota = listanota[-1]
        matricula = listanota[-2]
if nota < 8:
    print('Minimum note not reached')
else:
    print(int(matricula))
