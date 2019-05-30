n = list(map(int, input().split()))
t1 = n[0] * 60 + n[1]
t2 = n[2] * 60 + n[3]
if t2 <= t1:
    hf = ((t2 + 1440) - t1)//60
    mf = ((t2 + 1440) - t1) % 60
else:
    hf = (t2 - t1)//60
    mf = (t2 - t1) % 60
print('O JOGO DUROU {:.0f} HORA(S) E {:.0f} MINUTO(S)'. format(hf, mf), end='\n')
