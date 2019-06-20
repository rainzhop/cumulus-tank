# https://leetcode.com/problems/symmetric-tree/
#
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
# For example, this binary tree is symmetric:
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# But the following is not:
#     1
#    / \
#   2   2
#    \   \
#    3    3
#
# Note:
# Bonus points if you could solve it both recursively and iteratively.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        tmp = []
        tmp.insert(0, root.left)
        tmp.append(root.right)
        while tmp != []:
            left = tmp.pop(0)
            right = tmp.pop()
            if left == right == None:
                continue
            elif [left, right].count(None) == 1:
                return False
            if left.val != right.val:
                return False
            if left != None:
                tmp.insert(0, left.right)
                tmp.insert(0, left.left)
            if right != None:
                tmp.append(right.left)
                tmp.append(right.right)
        return True
