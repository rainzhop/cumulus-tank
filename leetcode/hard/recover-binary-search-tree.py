# https://leetcode.com/problems/recover-binary-search-tree/
#
# Two elements of a binary search tree (BST) are swapped by mistake.
#
# Recover the tree without changing its structure.
#
# Note:
# A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.a = None
        self.b = None
        self.pre = None

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.findWrongNode(root)
        self.a.val, self.b.val = self.b.val, self.a.val
        return

    def findWrongNode(self, root):
        if root is None:
            return
        if root.left is not None:
            self.findWrongNode(root.left)
        if self.pre is None:
            self.pre = root
        if self.pre.val > root.val:
            if self.a is None:
                self.a = self.pre
            self.b = root
        self.pre = root
        if root.right is not None:
            self.findWrongNode(root.right)
