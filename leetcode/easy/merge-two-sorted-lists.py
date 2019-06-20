# https://leetcode.com/problems/merge-two-sorted-lists/
#
# Merge two sorted linked lists and return it as a new list.
# The new list should be made by splicing together the nodes of the first two lists.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None and l2 == None: return None
        if l1 == None and l2 != None: return l2
        if l2 == None and l1 != None: return l1
        if l1.val > l2.val: l1, l2 = l2, l1
        head = l1
        last_l1, l1 = l1, l1.next
        while l2 != None and l1 != None:
            if l2.val < l1.val:
                tmp = l2.next
                last_l1.next, l2.next = l2, l1
                l2 = tmp
            else:
                last_l1, l1 = l1, l1.next
        return head
