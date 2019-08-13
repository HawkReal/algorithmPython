# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        length1 = self.getLength(pHead1)
        length2 = self.getLength(pHead2)
        if length1 == 0 or length2 == 0:
            return None

        if length2 > length1:
            dif = length2 - length1
            for i in range(0, dif):
                pHead2 = pHead2.next
        else:
            dif = length1 - length2
            for i in range(0, dif):
                pHead1 = pHead1.next
        while pHead1 != pHead2 and pHead1 and pHead2:
            pHead1 = pHead1.next
            pHead2 = pHead2.next

        if pHead1 == pHead2:
            return pHead1

        return None

    def getLength(self, pHead):
        count = 0
        if not pHead:
            return 0

        while pHead:
            count += 1
            pHead = pHead.next

        return count