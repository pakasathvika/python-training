'''ip:
      15 3 2 7 8 4
      m  t w t f s
   op:
       6
    '''
pr=0
prices=[15,3,2,7,8,4]
buy=prices[0]
for i in range(len(prices)):
    if prices[i]<buy:
        buy=prices[i]
    elif prices[i]-buy>pr:
        pr=prices[i]-buy
print(pr)

