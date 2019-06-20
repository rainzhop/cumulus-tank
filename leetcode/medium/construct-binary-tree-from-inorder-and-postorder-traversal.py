# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
# Given inorder and postorder traversal of a tree, construct the binary tree.
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
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        self.postorder = postRight[:]
        self.inorder = inorder[:]
        root = self.InPostOrder(0, len(inorder), 0, len(postorder))
        return root

    def InPostOrder(self, inLeft, inRight, postLeft, postRight):
        if inLeft == inRight or postLeft ==  postRight:
            return None
        rootVal = self.postorder[postRight - 1]
        root = TreeNode(rootVal)
        leftSize = self.inorder.index(rootVal) - inLeft
        rightSize = (inRight - inLeft) - leftSize - 1
        root.left = self.InPostOrder(inLeft, inLeft + leftSize, postLeft, postLeft + leftSize)
        root.right = self.InPostOrder(inLeft + leftSize + 1, inRight, postLeft + leftSize, postRight - 1)
        return root
