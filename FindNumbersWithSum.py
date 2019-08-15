# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        length = len(array)
        if not array or length == 0:
            return []

        begin = 0
        end = length - 1
        result = []
        while begin < end:
            currentSum = array[begin] + array[end]
            if currentSum == tsum:
                return [array[begin], array[end]]
            elif currentSum < tsum:
                begin += 1
            else:
                end -= 1

        return []

if __name__ == '__main__':
    solution = Solution()
    print(solution.FindNumbersWithSum([1,2,3,4,5],6))