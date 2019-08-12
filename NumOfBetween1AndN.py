# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        if n <= 0:
            return 0
        if n < 10 and n > 0:
            return 1

        str_num = str(n)
        length = len(str_num)
        first_num = str_num[0]
        if first_num == '1':
            num1 = n - self.tencifang(length - 1) + 1
        else:
            num1 = self.tencifang(length - 1)

        print(num1)
        num2 = int(first_num) * (length - 1) * self.tencifang(length - 2)
        print(num2)
        num3 = self.NumberOf1Between1AndN_Solution(n - int(first_num) * self.tencifang(length - 1))
        print(num3)

        return num1 + num2 + num3

    def tencifang(self, n):
        result = 1
        for i in range(0, n):
            result *= 10
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.NumberOf1Between1AndN_Solution(10))
