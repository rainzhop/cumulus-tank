# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
#
# Given a binary tree, flatten it to a linked list in-place.
#
# For example,
# Given
#
#          1
#         / \
#        2   5
#       / \   \
#      3   4   6
# The flattened tree should look like:
#    1
#     \
#      2
#       \
#        3
#         \
#          4
#           \
#            5
#             \
#              6
#
# Hints:
# If you notice carefully in the flattened tree,
# each node's right child points to the next node of a pre-order traversal.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root == None:
            return
        stack = []
        if root.right != None:
            stack.append(root.right)
        if root.left != None:
            stack.append(root.left)
        linkedNode = root
        while stack != []:
            node = stack.pop()
            linkedNode.left = None
            linkedNode.right = node
            if node.right != None:
                stack.append(node.right)
            if node.left != None:
                stack.append(node.left)
            linkedNode = node
        return
