# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
#
# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
#
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#
# Find the minimum element.
#
# You may assume no duplicate exists in the array.

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # --- first submit --- #
        # n = len(nums)
        # if n == 1: return nums[0]
        # for i in xrange(1, n):
        #     if nums[i] < nums[i - 1]:
        #         return nums[i]
        # return nums[0]
        # -------------------- #

        n = len(nums)
        left, right = 0, n - 1
        while right - left > 1:
            mid = (left + right) / 2
            if nums[mid] > [right]: left = mid
            if nums[left] > [mid]: right = mid
        return min(nums[left], nums[right])
