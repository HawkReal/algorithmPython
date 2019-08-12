# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index <= 0 :
            return 0
        ugly_list = [1]
        indexOfList = 1
        indexOfTwo = 0
        indexOfThree = 0
        indexOfFive = 0
        for i in range(indexOfList,index):
            ugly_list.append(min(ugly_list[indexOfTwo]*2,ugly_list[indexOfThree]*3,ugly_list[indexOfFive]*5))
            while ugly_list[indexOfTwo]*2 <= ugly_list[i]:
                indexOfTwo += 1
            while ugly_list[indexOfThree]*3 <= ugly_list[i]:
                indexOfThree += 1
            while ugly_list[indexOfFive]*5 <= ugly_list[i]:
                indexOfFive += 1

        print(ugly_list)
        return ugly_list[index-1]


if __name__ == '__main__':
    solution = Solution()
    solution.GetUglyNumber_Solution(3)