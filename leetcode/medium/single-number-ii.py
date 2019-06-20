# https://leetcode.com/problems/single-number-ii/
#
# Given an array of integers, every element appears three times except for one. Find that single one.
#
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for i in nums:
            d.setdefault(i, 0)
            d[i] = d[i] + 1
            if d[i] == 3:
                d.pop(i)
        return d.keys()[0]
