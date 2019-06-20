# https://leetcode.com/problems/binary-tree-paths/
#
# Given a binary tree, return all root-to-leaf paths.
#
# For example, given the following binary tree:
#    1
#  /   \
# 2     3
#  \
#   5
# All root-to-leaf paths are:
#
# ["1->2->5", "1->3"]
# Credits:
# Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        pathList = []
        def fillPathList(root, hdr):
            if root is None:
                return []
            if hdr == "":
                hdr = str(root.val)
            else:
                hdr = hdr + "->" + str(root.val)
            if root.left is None and root.right is None:
                pathList.append(hdr)
                return
            fillPathList(root.left, hdr)
            fillPathList(root.right, hdr)
        fillPathList(root, "")
        return pathList
