# https://leetcode.com/problems/validate-binary-search-tree/
#
# Given a binary tree, determine if it is a valid binary search tree (BST).
#
# Assume a BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        ok, a, b, = self.checkTree(root)
        return ok

    def checkTree(self, root):
        if root == None:
            return True, None, None
        leftOk, leftLeast, leftLargest = self.checkTree(root.left)
        rightOk, rightLeast, rightLargest = self.checkTree(root.right)
        if leftOk == False or rightOk == False:
            return False, None, None
        if leftLeast == None:
            least = root.val
        elif leftLargest > root.val:
            return False, None, None
        else:
            least = leftLeast
        if rightLeast == None:
            largest = root.val
        elif rightLeast < root.val:
            return False, None, None
        else:
            largest = rightLargest
        return True, least, largest
