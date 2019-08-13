# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        length = len(data)
        if not data or length <= 0:
            return 0

        firstIndex = self.getFirstIndex(data, length, k, 0, length - 1)
        lastIndex = self.getLastIndex(data, length, k, 0, length - 1)

        if firstIndex > -1 and lastIndex > -1:
            return lastIndex - firstIndex + 1

        return 0

    def getFirstIndex(self, data, length, k, start, end):
        if start > end:
            return -1
        midIndex = (start + end) / 2
        midData = data[midIndex]
        if midData == k:
            if midIndex > 0 and data[midIndex - 1] != k or midIndex == 0:
                return midIndex
            else:
                end = midIndex - 1
        elif midData > k:
            end = midIndex - 1
        else:
            start = midIndex + 1
        return self.getFirstIndex(data, length, k, start, end)

    def getLastIndex(self, data, length, k, start, end):
        if start > end:
            return -1

        midIndex = (start + end) / 2
        midData = data[midIndex]
        if midData == k:
            if midIndex < length - 1 and data[midIndex + 1] != k or midIndex == length - 1:
                return midIndex
            else:
                start = midIndex + 1
        elif midData < k:
            start = midIndex + 1
        else:
            end = midIndex - 1

        return self.getLastIndex(data, length, k, start, end)