# https://leetcode.com/problems/linked-list-cycle/
#
# Given a linked list, determine if it has a cycle in it.
#
# Follow up:
# Can you solve it without using extra space?

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        slow = head
        fast = head
        while True:
            slow = slow.next
            if fast.next != None:
                fast = fast.next.next
            else:
                return False
            
            if fast == None:
                return False
            if fast == slow:
                return True
            


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = head
    s = Solution()
    print s.hasCycle(head)
