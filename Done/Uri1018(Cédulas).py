din = int(input())
not100 = int(din/100)
not50 = int((din - 100 * not100)/50)
not20 = int((din - 100 * not100 - 50 * not50)/20)
not10 = int((din - 100 * not100 - 50 * not50 - 20 * not20)/10)
not5 = int((din - 100 * not100 - 50 * not50 - 20 * not20 - 10 * not10)/5)
not2 = int((din - 100 * not100 - 50 * not50 - 20 * not20 - 10 * not10 - 5 * not5)/2)
not1 = int((din - 100 * not100 - 50 * not50 - 20 * not20 - 10 * not10 - 5 * not5 - 2 * not2)/1)
print('{}\n{} nota(s) de R$ 100,00\n{} nota(s) de R$ 50,00\n{} nota(s) de R$ 20,00\n{} nota(s) de R$ 10,00\n{} nota(s) '
      'de R$ 5,00\n{} nota(s) de R$ 2,00\n{} nota(s) de R$ 1,00'
      .format(din, not100, not50, not20, not10, not5, not2, not1), end='\n')
