## 这是用来解决LC283,移动0的。
def move0(nums:list):
    i = 0
    j = len(nums) - 1
    results = [0] * len(nums)

    for index in range (len(nums)):
        if (nums[index] != 0):
            results[i] = nums[index]
            i += 1
        else :
            results[j] = nums[index]
            j -= 1
    nums = results
    return nums

if __name__ == '__main__':
    nums = list(map(int, input().split(",")))
    nums = move0(nums)
    print(nums)
