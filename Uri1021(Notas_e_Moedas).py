din = float(input())
not100 = int(din/100)
not50 = int((din - 100 * not100)/50)
not20 = int((din - 100 * not100 - 50 * not50)/20)
not10 = int((din - 100 * not100 - 50 * not50 - 20 * not20)/10)
not5 = int((din - 100 * not100 - 50 * not50 - 20 * not20 - 10 * not10)/5)
not2 = int((din - 100 * not100 - 50 * not50 - 20 * not20 - 10 * not10 - 5 * not5)/2)
rest = din - 100 * not100 - 50 * not50 - 20 * not20 - 10 * not10 - 5 * not5 - 2 * not2
print('NOTAS:\n{} nota(s) de R$ 100.00\n{} nota(s) de R$ 50.00\n{} nota(s) de R$ 20.00\n{} nota(s) de R$ 10.00\n{} '
      'nota(s) de R$ 5.00\n{} nota(s) de R$ 2.00'
      .format(not100, not50, not20, not10, not5, not2), end='\n')
moe100 = int(rest / 1)
moe50 = int((rest - moe100 * 1)/0.5)
moe25 = int((rest - moe100 * 1 - moe50 * 0.5)/0.25)
moe10 = int((rest - moe100 * 1 - moe50 * 0.5 - moe25 * 0.25)/0.1)
moe5 = int((rest - moe100 * 1 - moe50 * 0.5 - moe25 * 0.25 - moe10 * 0.1)/0.05)
moe1 = (rest - moe100 * 1 - moe50 * 0.5 - moe25 * 0.25 - moe10 * 0.1 - moe5 * 0.05)/0.01
print('MOEDAS:\n{} moeda(s) de R$ 1.00\n{} moeda(s) de R$ 0.50\n{} moeda(s) de R$ 0.25\n{} moeda(s) de R$ 0.10\n{} '
      'moeda(s) de R$ 0.05\n{:.0f} moeda(s) de R$ 0.01'.format(moe100, moe50, moe25, moe10, moe5, moe1), end='\n')
