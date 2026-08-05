## 这个是用来解决动态规划中，在m*n的网络中，不同路径的问题

import sys

def diff_path(m:int, n:int):
   # 注意，从左上走到右下，和从左下走到右上，理论上是一样的 

    dp = [[0]*(n+1) for _ in range (m+1)]
    dp[0][1] = 1 # 这个是第一行的路径，只有一条路径
    dp[1][0] = 1 # 这个是第一列的路径，只有一条路径

    for i in range (1,m+1):
        for j in range (1, n+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1] # 这个是从上面走下来，和从左边走过来的路径的和
            # dp[i][j] = dp[i-1][j] + dp[i][j+1]

    return dp 

if __name__ == '__main__':
    m ,n = map(int, input().split())
    dp = diff_path(m,n)
    print(dp)
