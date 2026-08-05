import sys

def steal_most(n:int ,steal:list):
    ## 这道题是用来做打家劫舍这道题的，用来获取小偷偷一排房间可以偷得的最大的金额
    dp = [0] * n
    for i in range (n):
        if i == 1: 
            value1 = 0
        if i == 0: 
            value1 = steal[0]
            value2 = 0

        value1 = dp[i-2] + steal[i] # 偷的情况
        value2 = dp[i-1]
        dp[i] = max(value1 , value2)

    return dp

if __name__ == '__main__':
    n = int( input().strip())
    steal = list(map(int, input().split()))
    dp = steal_most(n , steal)
    print(dp)
