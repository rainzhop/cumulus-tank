# https://leetcode.com/problems/reverse-linked-list/
#
# Reverse a singly linked list.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None: return None
        node, last = head.next, head
        while node != None:
            tmpNext = node.next
            node.next = last
            last = node
            node = tmpNext
        head.next = None
        return last
