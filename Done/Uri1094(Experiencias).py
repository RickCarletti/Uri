N = int(input())
totC = 0
totR = 0
totS = 0
quantT = 0
while N > 0:
    X = str(input())
    X = X.split()
    quant = int(X[0])
    quantT = quantT + quant
    cobaia = X[1]
    if cobaia == 'C':
        totC = totC + quant
    elif cobaia == 'R':
        totR = totR + quant
    elif cobaia == 'S':
        totS = totS + quant
    N = N - 1
print('Total: {} cobaias\nTotal de coelhos: {}\nTotal de ratos: {}\nTotal de sapos: {}\nPercentual de coelhos: {:.2f} %'
      '\nPercentual de ratos: {:.2f} %\nPercentual de sapos: {:.2f} %'
      .format(quantT, totC, totR, totS, (totC/quantT)*100, (totR/quantT)*100, (totS/quantT)*100), end='\n')
