# https://leetcode.com/problems/swap-nodes-in-pairs/
#
# Given a linked list, swap every two adjacent nodes and return its head.
#
# For example,
# Given 1->2->3->4, you should return the list as 2->1->4->3.
#
# Your algorithm should use only constant space.
# You may not modify the values in the list, only nodes itself can be changed.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None: return None
        if head.next != None:
            head = head.next
        last, node = None, head
        while node != None:
            if node.next != None:
                if last != None: last.next = node.next
                tmp = node.next
                node.next = node.next.next
                tmp.next = node
                last = node
                node = node.next
                print last.val, node.val
            else:
                break
        return head
