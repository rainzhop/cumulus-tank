# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
#
# Given a binary tree
#     struct TreeLinkNode {
#       TreeLinkNode *left;
#       TreeLinkNode *right;
#       TreeLinkNode *next;
#     }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
#
# Initially, all next pointers are set to NULL.
#
# Note:
# You may only use constant extra space.
# You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
#
# For example,
# Given the following perfect binary tree,
#          1
#        /  \
#       2    3
#      / \  / \
#     4  5  6  7
# After calling your function, the tree should look like:
#          1 -> NULL
#        /  \
#       2 -> 3 -> NULL
#      / \  / \
#     4->5->6->7 -> NULL

# Definition for binary tree with next pointer.
class TreeLinkNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if root == None:
            return
        nodes = []
        nodes.append(root)
        while nodes != []:
            tmp_nodes = []
            nodes_len = len(nodes)
            for i in range(nodes_len):
                if nodes[i].left == None:
                    break
                tmp_nodes.append(nodes[i].left)
                tmp_nodes.append(nodes[i].right)
                nodes[i].left.next = nodes[i].right
                if i + 1 == nodes_len:
                    nodes[i].right.next = None
                else:
                    nodes[i].right.next = nodes[i + 1].left
            nodes = tmp_nodes[:]


if __name__ == '__main__':
    root = TreeLinkNode(1)
    root.left = TreeLinkNode(2)
    root.left.left = TreeLinkNode(4)
    root.left.right = TreeLinkNode(5)
    root.right = TreeLinkNode(3)
    root.right.left = TreeLinkNode(6)
    root.right.right = TreeLinkNode(7)
    s = Solution()
    s.connect(root)

    print root.val, root.next
    print root.left.val, root.left.next.val, root.right.val, root.right.next
    print root.left.left.val, root.left.left.next.val, root.left.right.val, root.left.right.next.val, root.right.left.val, root.right.left.next.val, root.right.right.val, root.right.right.next
