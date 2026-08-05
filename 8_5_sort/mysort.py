# 这是一个用来练习排序算法的python

import sys

def my_bubble_sort(n:int, mylist:list):
    ## 这个是冒泡排序的解法
    for i in range (n):
        flag = bool(0)
        for j in range(n-i-1):
            ## 每一轮都交换数字，小的在左，大的在右，直到冒泡冒到最上面
            if mylist[j] > mylist[j+1]:
                tmp = mylist[j]
                mylist[j] = mylist[j+1]
                mylist[j+1] = tmp

    print(mylist)
    return

def my_select_sort(n:int, mylist:list):
    ## 这个是选择排序的做法
    for i in range (n):
        s_min = mylist[i]
        min_index = i
        for j in range(i+1,n):
            if mylist[j] < s_min:
                s_min = mylist[j]
                min_index = j 
        mylist[min_index] = mylist[i] 
        mylist[i] = s_min # 交换数据，将
    print(mylist)

def my_merge_sort(mylist:list):
    ## 这个是归并排序的做法
    if len(mylist)<=1 :
        return mylist
    mid = int(len(mylist)/2)
    left = mylist[:mid]
    left = my_merge_sort(left)
    right = mylist[mid:]
    right = my_merge_sort(right)

    mylist = merge_sort_result(left,right)
    return mylist

def merge_sort_result(left:list, right:list):
    result = []
    len_left = len(left)
    len_right = len(right)
    i = j = 0

    while i < len_left and j < len_right:
        if left[i] <= right [j]:
            result.append(left[i]) 
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])

    return result
     
def my_quick_sort(mylist:list):
    ## 这个是快速排序算法
    ## 假定选了第一个数据作为中间，让小于这个数据的排到左边，让大于这个数的排到右边
    if len(mylist) <= 1:
        return mylist
    
    left = 0
    right = len(mylist)-1
    mid_data = mylist[left] #假设取第一个元素作为最后的中间的元素
    while left < right:
        # 先从最右边找到一个比mid_data小的
        while right>left and mylist[right] > mid_data:
            right -= 1
        mylist[left] = mylist[right] 
        while left < right and mylist[left] < mid_data:
            left += 1
        mylist[right] = mylist[left] 
    mylist[left] = mid_data
    left_list = mylist[:left]
    right_list = mylist[right+1:] ## 注意right list这里要将下标往后再推一个, 不然就会陷入死循环中
    # mid = []
    # mid.append(mid_data)
    return my_quick_sort(left_list) + [mid_data] + my_quick_sort(right_list) ## 注意这里的mid_data要用[]括起来，否则数据类型就不统一了


if __name__ == '__main__':
    #n = int(input().strip())
    #print(n)
    #mylist = list(map(int, input().split()))
    ## 假设已经获取了数据
    n=10
    mylist = [9,7,3,4,1,2,8,0,5,6]
    print(mylist)
    #my_bubble_sort(n,mylist)
    #my_select_sort(n, mylist)
    #re = my_merge_sort(mylist)
    #print(re)
    re = my_quick_sort(mylist)
    print(re)

