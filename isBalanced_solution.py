# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    res = True

    def IsBalanced_Solution(self, pRoot):
        # write code here
        self.isBalanced(pRoot)
        return self.res

    def isBalanced(self, pRoot):
        if not pRoot:
            return 0
        if not self.res:
            return 1
        left = self.isBalanced(pRoot.left) + 1
        right = self.isBalanced(pRoot.right) + 1
        if abs(left - right) > 1:
            self.res = False

        return max(left, right)