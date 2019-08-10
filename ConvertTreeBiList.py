# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Convert(self, pRootOfTree):

        if not pRootOfTree:
            return None
        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree

        # 将左子树构建成双链表，返回链表头
        left = self.Convert(pRootOfTree.left)
        p = left

        # 定位至左子树的最右的一个结点
        while left and p.right:
            p = p.right

        # 如果左子树不为空，将当前root加到左子树链表
        if left:
            p.right = pRootOfTree
            pRootOfTree.left = p

        # 将右子树构造成双链表，返回链表头
        right = self.Convert(pRootOfTree.right)
        # 如果右子树不为空，将该链表追加到root结点之后
        if right:
            right.left = pRootOfTree
            pRootOfTree.right = right

        return left if left else pRootOfTree