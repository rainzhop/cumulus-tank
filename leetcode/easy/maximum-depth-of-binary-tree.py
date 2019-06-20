# https://leetcode.com/problems/maximum-depth-of-binary-tree/
#
# Given a binary tree, find its maximum depth.
#
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.left.right.left = TreeNode(5)
    root.right = TreeNode(6)
    s = Solution()
    print s.maxDepth(root)
