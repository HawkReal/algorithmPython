# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ""
        numbers = sorted(numbers)
        length = len(numbers)
        for i in range(0, length - 1):
            result = self.compat(numbers[i], numbers[i + 1])
            numbers[i + 1] = result

        return numbers[length - 1]

    def compat(self, number1, number2):
        str1 = str(number1) + str(number2)
        str2 = str(number2) + str(number1)
        return min(int(str1), int(str2))