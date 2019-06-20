# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
#
# Given a singly linked list where elements are sorted in ascending order,
# convert it to a height balanced BST.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head == None:
            return None
        array = []
        while head is not None:
            array.append(head.val)
            head = head.next
        root = self.sortedArrayToBST(array)
        return root

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        numsSize = len(nums)
        if numsSize == 0:
            return None
        if numsSize == 1:
            return TreeNode(nums[0])
        root = TreeNode(nums[numsSize/2])
        root.left = self.sortedArrayToBST(nums[:numsSize/2])
        root.right = self.sortedArrayToBST(nums[numsSize/2+1:])
        return root
