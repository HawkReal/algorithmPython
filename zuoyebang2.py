def minDistance(str1,str2):
    length1 = len(str1)
    length2 = len(str2)
    dp = [[0 for i in range(length1+1)] for j in range(length2+1)]
    i = 0
    for item in dp:
        item[0] = i
        i += 1
    i = 0
    for i in range(length1+1):
        dp[0][i] = i
        i += 1
    for i in range(1,length1+1):
        for j in range(1,length2+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                insert = 1 + dp[i][j-1]
                delete = 1 + dp[i-1][j]
                replace = dp[i-1][j-1] + 1
                dp[i][j] = min(insert,delete,replace)
    return dp[length1][length2]

if __name__ == '__main__':
    str_list = list(input().split())
    str1 = str_list[0]
    str2 = str_list[1]
    result = minDistance(str1,str2)
    print(result)