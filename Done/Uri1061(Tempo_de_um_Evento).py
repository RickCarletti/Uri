dia1 = list(map(str, input().split()))
hrs1 = list(map(int, input().split(' : ')))
dia2 = list(map(str, input().split()))
hrs2 = list(map(int, input().split(' : ')))
dia1 = int(dia1[1])
dia2 = int(dia2[1])
diar = dia2 - dia1
hrsr = hrs2[0] - hrs1[0]
minr = hrs2[1] - hrs1[1]
segr = hrs2[2] - hrs1[2]
if segr < 0:
    segr = segr + 60
    minr = minr - 1
if minr < 0:
    minr = minr + 60
    hrsr = hrsr - 1
if hrsr < 0:
    hrsr = hrsr + 24
    diar = diar - 1
print('{} dia(s)\n{} hora(s)\n{} minuto(s)\n{} segundo(s)'.format(diar, hrsr, minr, segr), end='\n')
