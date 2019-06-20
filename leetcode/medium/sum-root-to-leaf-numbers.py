# https://leetcode.com/problems/sum-root-to-leaf-numbers/
#
# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
#
# An example is the root-to-leaf path 1->2->3 which represents the number 123.
#
# Find the total sum of all root-to-leaf numbers.
#
# For example,
#     1
#    / \
#   2   3
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
#
# Return the sum = 12 + 13 = 25.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        sumList = self.sumNumList(root)
        sumList = [eval(num.lstrip('0')) for num in sumList]
        return sum(sumList)

    def sumNumList(self, root):
        sumList = []
        if root == None:
            pass
        elif root.left == None and root.right == None:
            sumList.append(str(root.val))
        else:
            sumList.extend(self.sumNumList(root.left))
            sumList.extend(self.sumNumList(root.right))
            sumList = [str(root.val) + str(i) for i in sumList]
        return sumList
