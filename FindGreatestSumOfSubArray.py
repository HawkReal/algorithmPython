# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        length = len(array)
        dp = [i for i in array]
        for i in range(1, length):
            dp[i] = max(dp[i - 1] + array[i], array[i])

        return max(dp)