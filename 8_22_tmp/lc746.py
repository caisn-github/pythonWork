import sys

## 做dp的动态规划的入门题目
if __name__ == '__main__':
    cost = list(map(int, input().split(',')))
    dp = [0] * (len(cost) + 1)
    if len(cost) <= 1:
        print(0) 

    ## 开始动态规划
    dp[0] = 0
    dp[1] = 0 
    for i in range(2 ,len(cost)+1):
        dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
    print(dp)
    
