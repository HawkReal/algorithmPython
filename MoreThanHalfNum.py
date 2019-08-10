# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        length = len(numbers)
        # write code here
        if not numbers:
            return 0
        number = 1
        moreOfHalf = numbers[0]
        for i in range(1,length):
            if number == 0:
                number = 1
                moreOfHalf = numbers[i]
            elif numbers[i] == moreOfHalf:
                number += 1
            else:
                number -= 1
        if self.checkIsHalf(numbers,moreOfHalf,length):
            return moreOfHalf
        else:
            return 0
    def checkIsHalf(self,numbers,number,length):
        times = 0
        for i in range(0,length):
            if numbers[i] == number:
                times += 1
        if times*2<=length:
            return False
        else:
            return True