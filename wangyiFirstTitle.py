#网易提前批笔试第一道题
if __name__ == '__main__':
    n = int(input())
    list1 = list(map(int,input().split()))
    list2 = [0]*n
    for i in range(0,n):
        list2[i] = n-list1[i]+1

    print(list2)
