''' ip:
        [2,3,5,6]           only with 1 2rs coin,1,3rs coin,1 5rs coin , 1 6rs coin
        11             can 11 rs made by using those 2,3,4,5 rs coins or not ?
    explaination
        
        0 1 2 3 4 5 6 7 8 9 10 11
    2   1 0 1 0 0 0 0 0 0 0  0  0
    3   1 0 1 1 0 1 0 0 0 0  0  0
    5   1 0 1 1 0 1 0 1 1 0  1  0
    6   1 0 1 1 0 1 1 1 1 1  1  1
    op:
        yes   '''
def can_make_amount_with_limited_coins(coins, target):
    n=len(coins)
    dp=[[False]*(target+ 1) for _ in range(n + 1)]
    dp[0][0]=True
    for i in range(1,n+1):
        coin = coins[i-1]
        for j in range(target + 1):
            if dp[i - 1][j]:
                dp[i][j] = True 
            if j >= coin and dp[i - 1][j - coin]:
                dp[i][j] = True  
    return dp[n][target]
coins = [2, 3, 5, 6]
target = 7
result = can_make_amount_with_limited_coins(coins, target)
print("Yes" if result else "No")
