# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if not s:
            return ""

        length = len(s)
        s1 = s[:n]
        s2 = s[n:]
        return s2 + s1