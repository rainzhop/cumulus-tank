# https://leetcode.com/problems/minimum-depth-of-binary-tree/
#
# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        shortestNum = -1
        num = 0
        node = root
        while True:
            num += 1
            if node.left == None and node.right == None:
                shortestNum = num
                break
            node = node.left

        stack = []
        pathNum = []
        stack.append(root)
        pathNum.append(0)
        num = 0
        while stack != []:
            node = stack.pop()
            num += pathNum.pop() + 1
            print node,num
            if node.left == None and node.right == None:
                # leaf
                if shortestNum > num:
                    shortestNum = num
                continue
            if node.right != None:
                stack.append(node.right)
                pathNum.append(num)
            if node.left != None:
                stack.append(node.left)
                pathNum.append(num)

        return shortestNum
