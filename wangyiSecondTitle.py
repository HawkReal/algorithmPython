#网易笔试第二题
if __name__ == '__main__':
    t = int(input())
    while t>0:
        n = int(input())
        list1 = [0]*n
        list1 = list(map(int,input().split()))
        list1.sort()

        temp = list1[n-1]
        list1[n-1] = list1[n-2]
        list1[n-2] = temp

        isSuccess = True
        for i in range(0,n):
            pre = (i-1+n)%n
            next = (i+1)%n
            if list1[pre]+list1[next] < list1[i]:
                isSuccess = False

        if isSuccess:
            print(True)
        else:
            print(False)

        t -= 1
