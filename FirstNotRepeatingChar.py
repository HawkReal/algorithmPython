# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if not s:
            return -1
        dic = [0]*256
        for i in s:
            dic[ord(i)] += 1
        for j in s:
            if dic[ord(j)] == 1:
                return s.index(j)
        return -1