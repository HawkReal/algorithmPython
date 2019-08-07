# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        result = []
        path = []
        currentNumber = 0

        def findPath(root, expectNumber, currentNumber, path):
            isLeaf = root.left is None and root.right is None
            currentNumber += root.val
            path.append(root)

            if currentNumber == expectNumber and isLeaf:
                onePath = []
                for node in path:
                    onePath.append(node.val)
                result.append(onePath)

            if currentNumber < expectNumber:
                if root.left:
                    findPath(root.left, expectNumber, currentNumber, path)
                if root.right:
                    findPath(root.right, expectNumber, currentNumber, path)
            path.pop()

        findPath(root, expectNumber, currentNumber, path)
        return result



#定义一个追踪列表，定义一个最终结果列表。
#当前节点的值如果等于最终结果，并且此节点为叶子节点，则将追踪列表加入到最终结果列表中。
#如果不满足上面的条件，判断该节点的左右子节点是否为空，如果不为空，则递归下面的子节点，并且最终结果减去当前节点的值
#最后将追踪列表中的最上面的节点取出，栈的特性。