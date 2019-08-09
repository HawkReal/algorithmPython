#只要数组中既有奇数又有偶数，直接对数组排序即可
if __name__ == '__main__':
    n = int(input())
    odd_num = 0
    even_num = 0
    list1 = list(map(int,input().split()))
    for i in range(0,len(list1)):
        if list1[i] % 2 == 1:
            odd_num += 1
        else:
            even_num += 1

    if odd_num > 0 and even_num > 0:
        list1.sort()

    print(list1)