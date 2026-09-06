import sys

re = []
r = []

def lc_46(nums:list[int]):
    ## 这道题是用来做回溯与递归的计算的
    if len(nums) == 0:
        re.append(r) 
        return 

    for i in range(len(nums)):
        value = nums[i]
        print(value)
        r.append(value)
        tmp = nums[i:]
        print(tmp)
        lc_46(tmp)
        r.pop()
        

    return re


if __name__ == '__main__':
    nums = list(map(int, input().split()))
    re = lc_46(nums)
    print(re)
