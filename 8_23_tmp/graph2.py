import sys
INF = 10**9 ##表示不可达

def djs(edges,m):
    ## 然后从看其他的点到第一个顶点的距离
    dist = [INF] * (m+1) ## 应该是乘上顶点的数量，这样就是从顶点0到其他顶点了
    dist[1] = 0 ## 从自己到自己是0

    for _ in range(2*m):
        for start,end,w in edges:
            if dist[end] > dist[start] + w:
                dist[end] = dist[start] + w

    return dist


if __name__ == '__main__':
    edges = []
    ## 然后开始输入图
    n = 4 

    for i in range(n):
        nums = list(map(int ,input().split()))
        u,v,w = nums[0],nums[1],nums[2]
        edges.append((u,v,w))

    ## 这样图就构建完毕了
    dist = djs(edges, 4)
    print(dist)
