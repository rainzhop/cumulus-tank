# https://leetcode.com/problems/find-the-duplicate-number/
#
# Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive),
# prove that at least one duplicate number must exist.
# Assume that there is only one duplicate number, find the duplicate one.
#
# Note:
# You must not modify the array (assume the array is read only).
# You must use only constant, O(1) extra space.
# Your runtime complexity should be less than O(n2).
# There is only one duplicate number in the array, but it could be repeated more than once.
#
# Credits:
# Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 1, len(nums) - 1
        while True:
            b = (left + right) / 2
            lt = gt = eq = 0
            for i in nums:
                if i < left or i > right: continue
                if i < b: lt += 1
                elif i > b: gt += 1
                else: eq += 1
            if eq > 1: return b
            if lt >= gt: right = b - 1
            elif lt < gt: left = b + 1
            if left == right: return left

if __name__ == '__main__':
    nums = [1,2,3,4,5,6,8,7,8,9]
    s = Solution()
    print s.findDuplicate(nums)
