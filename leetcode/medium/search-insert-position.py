# https://leetcode.com/problems/search-insert-position/
#
# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
#
# You may assume no duplicates in the array.
#
# Here are few examples.
# [1,3,5,6], 5 -> 2
# [1,3,5,6], 2 -> 1
# [1,3,5,6], 7 -> 4
# [1,3,5,6], 0 -> 0

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        if target > nums[n/2]:
            if n == 1:
                return 1
            else:
                return n/2 + 1 + self.searchInsert(nums[n/2 + 1:], target)
        elif target < nums[n/2]:
            if n == 1:
                return 0
            else:
                return self.searchInsert(nums[:n/2], target)
        elif target == nums[n/2]:
            return n/2
