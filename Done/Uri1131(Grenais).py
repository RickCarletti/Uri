rept = 1
tot = 0
gremio_win = 0
inter_win = 0
empate = 0
while rept == 1:
    inter, gremio = map(int, input().split())
    tot = tot + 1
    if gremio > inter:
        gremio_win = gremio_win + 1
    elif inter > gremio:
        inter_win = inter_win + 1
    else:
        empate = empate + 1
    rept = int(input('Novo grenal (1-sim 2-nao)'))
    print()
print('{} grenais\nInter:{}\nGremio:{}\nEmpates:{}'.format(tot, inter_win, gremio_win, empate))
if gremio_win > inter_win:
    print('Gremio venceu mais', end='\n')
elif inter_win > gremio_win:
    print('Inter venceu mais', end='\n')
else:
    print('Nao houve vencedor', end='\n')
