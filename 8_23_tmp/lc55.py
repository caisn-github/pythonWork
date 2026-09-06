import sys
#from collections import defaultdict
if __name__ == '__main__':
    nums = list(map(int ,input().split(',')))
    max_reach = nums[0] ## 最开始能到达的就是第一个格子可以到达的

    i=0
    while i < max_reach:
        print(max_reach)
        if nums[i] + i > max_reach:
            max_reach = nums[i] + i
        i += 1
    if max_reach >= (len(nums) - 1):
        print("true")
    else:
        print("false")

