import sys
from collections import defaultdict

if __name__ == '__main__':
    nums = list(map(int, input().split(',')))
    target = int(input())

    m = defaultdict(list)
    for i in range(len(nums)):
        m[nums[i]].append(i)
    
    nums = sorted(nums)
    ## 接着就可以启动双向指针来查找了

    slow = 0
    quick = len(nums)-1
    while quick>slow:
        if nums[quick] + nums[slow] == target:
            if nums[quick] == nums[slow]:
                po1 = m[nums[quick]][0]
                po0 = m[nums[quick]][1]
                print(po1)
                print(po0)
                break
            print(m[nums[quick]])
            print(m[nums[slow]])
            break
        elif nums[quick] + nums[slow] > target:
            quick -= 1
        else:
            slow += 1

