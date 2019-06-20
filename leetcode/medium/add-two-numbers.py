# https://leetcode.com/problems/add-two-numbers/
#
# You are given two linked lists representing two non-negative numbers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2, carry = 0):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None and l2 == None and carry == 0:
            return None
        if l1 == None:
            l1 = ListNode(0)
        if l2 == None:
            l2 = ListNode(0)

        ret = ListNode(0);
        ret.val = l1.val + l2.val + carry

        carry = ret.val / 10
        if carry > 0:
            ret.val = ret.val % 10
        ret.next = self.addTwoNumbers(l1.next, l2.next, carry)

        return ret
