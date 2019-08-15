# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        if tsum < 3:
            return None

        begin = 1
        end = 2
        mid = (tsum + 1) / 2
        number_list = []

        numberOfSum = begin + end
        while begin < mid:
            if numberOfSum == tsum:
                number_list.append(self.gen_list(begin,end))
            while numberOfSum > tsum and begin < mid:
                numberOfSum -= begin
                begin += 1
                if numberOfSum == tsum:
                    number_list.append(self.gen_list(begin,end))
            end += 1
            numberOfSum += end
        return number_list
    def gen_list(self,begin,end):
        number_list = []
        for i in range(begin,end+1):
            number_list.append(i)
        return number_list


if __name__ == '__main__':
    solution = Solution()
    print(solution.FindContinuousSequence(3))