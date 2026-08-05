import sys


def LC_70(n:int):
    idp = [0] * n
    if n <= 1:
        return 1
    idp[0] = 1 # 这个是为了方便进行初始化
    idp[1] = 1
    for i in range (2,n):
        idp[i] = idp[i-1] + idp[i-2]
    
    return idp


def bag01(n:int, V:int, v: list[int], w:list[int]):
    ## 这个背包是用来zhaodaozhaodao

    # 首先需要声明一个二维的数组
    s = [[0] * (V+1) for _ in range (n+1)]
    # 假设当前的这个不放，假设当前的这个要放
    for i in range (1,n+1):
        for j in range (1,V+1):
            value1 = s[i-1][j] # 不放当前的这个物品
            value2 = s[i-1][j-v[i]] + w[i] if j >= v[i] else 0 # 放当前的这个物品，注意要先判断下，J是不是比当前的v大，否则会出现在背包空间不足就可以直接塞下一个的情况。
            s[i][j] = max(value1, value2)
    return s 

def bag02(n:int, V:int, v:list[int], w:list[int]):
    # 怎么样做到刚好装下这个，空间背包刚好是满的，并且装的东西是最大的
    s = [[0] * (V+1) for _ in range (n+1)]
    for j in range (1,V+1):
        flag = [0] * (n+1) # 用来表示在这一轮装包中，是否已经装过了这个物品
        for i in range (1,n+1):
            if j == v[i] and flag[i] == 0:
                s[i][j] = w[i]
                flag[i] = 1
            elif j>= v[i] and s[i-1][j-v[i]] >0 and flag[i] == 0:
                s[i][j] = s[i-1][j-v[i]] + w[i]
                flag[i] = 1
            ## 其他情况，数据都是0 
    return s 

if __name__ == '__main__':
    n, V = map(int, input().split())
    v = [0] * (n+1)# 用来存放每个物品对应的体积
    w = [0] * (n+1)# 用来存放每个物品对应的价值
    v[0] = 0 
    w[0] = 0 
    for i in range (1,n+1) :
        v[i],w[i] = map(int, input().split())
    # print(v)
    # print(w)

    s = bag01(n, V, v, w)
    re1 = s[n][V]
    s2 = bag02(n, V, v, w)
    re2 = s2[n][V]

    print(re1)
    print(re2)
    # print(s)
    # print(s2)

