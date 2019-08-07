# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        length = len(sequence)
        if sequence is None or length == 0:
            return False

        root = sequence[length - 1]
        i = 0
        while i < length - 1:
            if sequence[i] > root:
                break
            i += 1
        for j in range(i, length - 1):
            if sequence[j] < root:
                return False
        left = True
        right = True
        if i > 0:
            left = self.VerifySquenceOfBST(sequence[:i])
        if i < length - 1:
            right = self.VerifySquenceOfBST(sequence[i:length - 1])
        return left and right


#找到序列中的根节点，然后从序列的首节点开始比较，直到找到比根节点大的节点为右子树的第一个节点。从这个节点开始到根节点之前，如果出现了比根节点小的节点，则返回false
#用递归的方法再分别判断左子树和右子树