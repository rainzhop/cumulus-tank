# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# Given preorder and inorder traversal of a tree, construct the binary tree.
#
# Note:
# You may assume that duplicates do not exist in the tree.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        self.preorder = preorder[:]
        self.inorder = inorder[:]
        root = self.PreInOrder(0, len(preorder), 0, len(inorder))
        return root

    def PreInOrder(self, preLeft, preRight, inLeft, inRight):
        if preLeft == preRight or inLeft == inRight:
            return None
        rootVal = self.preorder[preLeft]
        root = TreeNode(rootVal)
        leftSize = self.inorder.index(rootVal) - inLeft
        rightSize = (inRight - inLeft) - leftSize - 1
        root.left = self.PreInOrder(preLeft + 1, preLeft + leftSize + 1, inLeft, inLeft + leftSize)
        root.right = self.PreInOrder(preLeft + leftSize + 1, preRight, inLeft + leftSize + 1, inRight)
        return root
