# https://leetcode.com/problems/binary-tree-inorder-traversal/
#
# Given a binary tree, return the inorder traversal of its nodes' values.
#
# For example:
# Given binary tree {1,#,2,3},
#    1
#     \
#      2
#     /
#    3
# return [1,3,2].
#
# Note: Recursive solution is trivial, could you do it iteratively?
#
# confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.
#
# OJ's Binary Tree Serialization:
# The serialization of a binary tree follows a level order traversal, where '#' signifies a path terminator where no node exists below.
#
# Here's an example:
#    1
#   / \
#  2   3
#     /
#    4
#     \
#      5
# The above binary tree is serialized as "{1,2,3,#,#,4,#,#,5}".

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
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
            if type(node) == int:
                traversal.append(node)
            else:
                if node.left != None:
                    if node.right != None:
                        node_path.append(node.right)
                    node_path.append(node.val)
                    node = node.left
                    continue
                elif node.right != None:
                    traversal.append(node.val)
                    node = node.right
                    continue
                else:
                    traversal.append(node.val)

            if node_path == []:
                break
            node = node_path.pop()

        return traversal

if __name__ == '__main__':
    root = TreeNode(1)
    #root.left = TreeNode(2)
    #root.left.left = TreeNode(3)
    #root.left.right = TreeNode(4)
    root.right = TreeNode(5)
    #root.right.left = TreeNode(6)
    #root.right.right = TreeNode(7)
    s = Solution()
    print s.inorderTraversal(root)
