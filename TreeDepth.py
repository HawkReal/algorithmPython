# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot:
            return 0

        left = self.TreeDepth(pRoot.left)
        right = self.TreeDepth(pRoot.right)

        if left > right:
            return left + 1
        else:
            return right + 1