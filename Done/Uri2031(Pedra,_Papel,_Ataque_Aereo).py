for i in range(int(input())):
    j1 = input()
    j2 = input()
    if j1 == 'ataque' and j1 == j2:
        print('Aniquilacao mutua')
    elif j1 == 'pedra' and j2 == j1:
        print('Sem ganhador')
    elif j1 == 'papel' and j2 == j1:
        print('Ambos venceram')
    elif (j1 == 'ataque' or j1 == 'pedra') and (j2 == 'pedra' or j2 == 'papel'):
        print('Jogador 1 venceu')
    elif (j2 == 'ataque' or j2 == 'pedra') and (j1 == 'pedra' or j1 == 'papel'):
        print('Jogador 2 venceu')
