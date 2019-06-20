# https://leetcode.com/problems/delete-node-in-a-linked-list/
#
# Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.
#
# Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node with value 3, the linked list should become 1 -> 2 -> 4 after calling your function.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

if __name__ == '__main__':
    first = ListNode(1)
    second = ListNode(2)
    first.next = second
    third = ListNode(3)
    second.next = third
    fourth = ListNode(4)
    third.next = fourth
    s = Solution()
    s.deleteNode(third)

    print first.val, first.next.val, first.next.next.val
