from collections import Counter


def func_01():
    ## 将字符串“12345”转化为整数并相加
    s = "12345"
    list_s = list(s)
    result = 0
    for c in s:
        result += int(c)
    print(result)

        


if __name__ == '__main__':
    func_01()
    data = ['a','z','a']
    counter = Counter(data)
    print(data)
    print(counter)
    print(counter['a'])
