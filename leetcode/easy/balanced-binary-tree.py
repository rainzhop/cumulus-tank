# https://leetcode.com/problems/balanced-binary-tree/
#
# Given a binary tree, determine if it is height-balanced.
#
# For this problem, a height-balanced binary tree is defined as a binary tree
# in which the depth of the two subtrees of every node never differ by more than 1.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        treeHeight, balance = self.checkBalance(root)
        return balance

    def checkBalance(self, node):
        if node == None:
            return 0, True
        leftSize, leftBalance = self.checkBalance(node.left)
        rightSize, rightBalance = self.checkBalance(node.right)
        if leftSize - rightSize in [-1, 0, 1] and leftBalance and rightBalance:
            return max(leftSize, rightSize) + 1, True
        else:
            return 0, False
