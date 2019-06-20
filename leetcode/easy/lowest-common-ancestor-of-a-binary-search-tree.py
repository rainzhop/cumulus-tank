# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
#
# Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
#
# According to the definition of LCA on Wikipedia:
# “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”
#
#         _______6______
#        /              \
#     ___2__          ___8__
#    /      \        /      \
#    0      _4       7       9
#          /  \
#          3   5
# For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6.
# Another example is LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        top = root
        while True:
            if self.isDescendant(top.left, p) and self.isDescendant(top.left, q):
                top = top.left
                continue
            elif self.isDescendant(top.right, p) and self.isDescendant(top.right, q):
                top = top.right
                continue
            break
        return top


    def isDescendant(self, top, node):
        if top == None:
            return False
        elif top == node or top.left == node or top.right == node:
            return True
        else:
            return self.isDescendant(top.left, node) or self.isDescendant(top.right, node)


if __name__ == '__main__':
    top = TreeNode(1)
    top.left = TreeNode(2)
    top.right = TreeNode(3)
    top.left.left = TreeNode(4)
    top.left.right = TreeNode(5)
    top.left.right.right = TreeNode(6)
    p = top.right
    q = top.left.right.right
    s = Solution()
    print s.lowestCommonAncestor(top, p, q).val
