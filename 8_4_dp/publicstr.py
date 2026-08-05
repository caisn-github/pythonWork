## 这个是用来解决最长公共子序列的问题的

import sys

## 接下来算法是用来处理公共字符串的
def public_str(str1:str, str2:str):
    len1 = len(str1)
    len2 = len(str2)
    
    s = [[0] * len2 for _ in range(len1)]
    for i in range (len1):
        for j in range (len2):
            if str1[i] != str2[j]: # 假设直接就是不相等的情况
                if i==0 :
                    s[i][j] = 0
                else : s[i][j] = max(s[i-1][j],s[i][j-1]) # 这个是取上一个的最大值, 注意它的max值是在没有没有相等的情况下，要去决定从哪里跳转, 注意这里要跳转的是[i-1][j]和[i][j-1]，因为我们要去取上一个的最大值
            else :
                if i==0 or j==0 :
                    s[i][j] = 1 
                else :s[i][j] = s[i-1][j-1] + 1 # 假设这个字符相等了，我要去取这个字符

    return s

if __name__ == '__main__':
    str1,str2=map(str, input().split(","))
    str1 = str1.strip('"')
    str2 = str2.strip('"')
    s = public_str(str1, str2)
    print(s)
