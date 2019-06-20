# https://leetcode.com/problems/move-zeroes/
#
# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
# For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].
#
# Note:
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
# Credits:
# Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zeroIdx = -1 # to record first index of 0
        total_len = len(nums)
        for i in range(total_len):
            if nums[i] == 0:
                if (nums[i - 1] != 0 and i > 0) or i == 0:
                    zeroIdx = i # only execute once, to find the first zero and record its index
            elif nums[i] != 0:
                if zeroIdx == -1:
                    continue
                nums[zeroIdx] = nums[i]
                nums[i] = 0
                zeroIdx = zeroIdx + 1


if __name__ == '__main__':
    nums = [0,1,4,0,6,0]
    s = Solution()
    s.moveZeroes(nums)
    print nums
