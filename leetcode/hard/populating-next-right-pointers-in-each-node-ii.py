# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
#
# Follow up for problem "Populating Next Right Pointers in Each Node".
#
# What if the given tree could be any binary tree? Would your previous solution still work?
#
# Note:
# You may only use constant extra space.
# For example,
# Given the following binary tree,
#          1
#        /  \
#       2    3
#      / \    \
#     4   5    7
# After calling your function, the tree should look like:
#          1 -> NULL
#        /  \
#       2 -> 3 -> NULL
#      / \    \
#     4-> 5 -> 7 -> NULL

## Definition for binary tree with next pointer.
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
        pre = root
        while pre != None:
            node = pre
            while node != None:
                if node.left != None and node.right != None:
                    node.left.next = node.right
                nextNode = node.next
                while nextNode != None:
                    if nextNode.left != None:
                        if node.right != None:
                            node.right.next = nextNode.left
                        elif node.left != None:
                            node.left.next = nextNode.left
                    elif nextNode.right != None:
                        if node.right != None:
                            node.right.next = nextNode.right
                        elif node.left != None:
                            node.left.next = nextNode.right
                    else:
                        nextNode = nextNode.next
                        continue
                    break
                node = node.next
            while True:
                if pre.left != None:
                    pre = pre.left
                elif pre.right != None:
                    pre = pre.right
                elif pre.next != None:
                    pre = pre.next
                    continue
                else:
                    pre = None
                break
        return

if __name__ == '__main__':
    root = TreeLinkNode(1)
    root.left = TreeLinkNode(2)
    root.right = TreeLinkNode(3)
    root.left.left = TreeLinkNode(4)
    root.left.right = TreeLinkNode(5)
    root.left.left.left = TreeLinkNode(7)
    root.right.right = TreeLinkNode(6)
    root.right.right.right = TreeLinkNode(8)
    s = Solution()
    s.connect(root)

    print root.left.left.left.next.val
