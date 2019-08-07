
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        queueData = []
        result = []
        if root is not None:
            queueData.append(root)
        while queueData:
            node = queueData.pop(0)
            result.append(node.val)
            if node.left is not None:
                queueData.append(node.left)
            if node.right is not None:
                queueData.append(node.right)

        return result


#用一个队列来存储树的节点，先存入根节点，随后进入循环，当队列不为空的时候，循环开始，取出队列的第一个节点，并打印其值。
#然后判断其左右节点是否为空，再按照顺序依次将左右节点存入到队列中。