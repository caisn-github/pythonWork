## 这个是用来解决leetcode的动态规划题库，5.最长回文子串的
import sys

def returnStr(line: list, line2:list):
    len_line = len(line)

    dp = [[0] * (len_line + 1) for _ in range (len_line+1)]
    for i in range(1, len_line+1): ## 为了在第一次计算，line的第一个字符的下标是0的情况的预防
        for j in range(1,len_line+1):
            if line[i-1] == line2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1 # 这里出问题了，这里不对，因为假设前面的就不是呢?
            else :
                dp[i][j] = 0 ## 假设不等，那么就取少一个字符的时候的最大值，注意dp[i-1][j-1]一定比这俩小
    return dp

def find_first_pos(dp):
    ## 然后找到回文最早开始的位置
    ## 即找到在dp这个二维数组中，最大的数字最早开始的位置
    len_dp = len(dp) # 找到dp的第一维的长度
    max_i = 0
    max_j = 0
    max_value = 0 
    for i in range (len_dp):
        for j in range(len_dp):
            if dp[i][j] > dp[max_i][max_j]:
                max_i = i
                max_j = j
    max_value = int(dp[max_i][max_j])
    print(max_i)
    print(max_j)
    print(max_value)
    return int(max_i), int(max_value)

if __name__ == '__main__':
    line = input().strip()
    line2 = line[::-1] ## 从0到len之间进行逆转
    
    ## 通过这种方式，就将这个动态规划转化为二维的，
    ## 转化为二维的，求str1与str2之间连续一致的最长公共子串的问题了
    dp = returnStr(line,line2)
    max_i,max_value = find_first_pos(dp) ## 那么最后找到的，max_i就是起始地址，max_j就是结束地址
    big_str = line[max_i-max_value:max_i] ## 减去是因为这是已经把最长回文子串遍历完毕了 而max_j不用，因为list不会遍历到max_j
    print(dp)
    print(big_str)
