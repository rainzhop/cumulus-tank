# https://leetcode.com/problems/binary-tree-preorder-traversal/
#
# Given a binary tree, return the preorder traversal of its nodes' values.
#
# For example:
# Given binary tree {1,#,2,3},
#    1
#     \
#      2
#     /
#    3
# return [1,2,3].
#
# Note: Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        traversal = []
        node = root
        node_path = []
        while True:
            if node != None:
                traversal.append(node.val)

            if node.left != None:
                if node.right != None:
                    node_path.append(node.right)
                node = node.left
            elif node.right != None:
                node = node.right
            else:
                if node_path == []:
                    break
                node = node_path.pop()

        return traversal


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    s = Solution()
    print s.preorderTraversal(root)
