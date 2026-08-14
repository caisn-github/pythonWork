### 对应zero2leetcode网站上的双指针
import sys

## 这道题使用暴力解法也是可以的，但是因为给定的数组有序，所以此时就可以使用
## 双头遍历的做法，可以将复杂度从原本的n2变成n。这减少了原本的就没有必要的遍历
def twoSum(numbers:list[int], target:int):
    ## 注意number就是一个升序的数组
    i = 0
    j = len(numbers) - 1 
    ## 使用双指针进行遍历

    flag = bool(0)
    while i < j:
        if numbers[i] + numbers[j] < target:
            i += 1
        elif numbers[i] + numbers[j] > target:
            j -= 1
        else : 
            flag = bool(1)
            break
    if flag:
        return numbers[i],numbers[j]

def threeSum(nums:list[int]):
    ## 对应LC15 三数之和，假设做过两数之和的双头遍历，就可以把复杂度从n3变成n2
    ## 对于n3的解法：固定两个数，找另外一个数；对于n2的解法：固定一个数，双头o找另外两个数
    ## 这道题就是经典的看起来题目好做，但是非常繁琐，因为不允许重复，所以剪枝是个很重要的事
    nums = sorted(nums) ##因为双头法是针对本就规律的数据的
    results = []
    len_num = len(nums)
    for i in range (len_num):
        if i >= 1 and nums[i] == nums[i-1]:
            ## 说明这个i已经处理过了
            continue
        
        ## 先固定一个数，然后用双头去找另外两个数
        j = i+1 ## 避免后续的重复
        k = len_num-1 
        while j < k :
            
            if (nums[j] + nums[i] + nums[k]) == 0:
                tmp = []
                tmp.append(nums[i])
                tmp.append(nums[j])
                tmp.append(nums[k])
                results.append(tmp)
                ## ************************
            ### 这里也要跳过重复的j、k，important
                j += 1
                k -= 1 ##各自跳开
                while j < k and nums[j] == nums[j-1]:
                    j += 1
                while j < k and k <= len_num-2 and nums[k] == nums[k+1]:
                    k -= 1
                ## 在这种情况下，随意调整一个j或者k，随意调整一个，因为题目说了不能再相等了
            elif (nums[i] + nums[j] + nums[k]) < 0:  ### 注意这里也要跳过重复的j\k
                j += 1
            elif (nums[i] + nums[j] + nums[k]) > 0:
                k -= 1
            
    
            
            
    return results

# 还需要再做剪枝的操作，但是怎么剪枝呢？


if __name__ == '__main__':
    nums = [-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]
    #nums = map(int(), input().split())
    results = threeSum(nums)
    print(results)

