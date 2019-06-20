# https://leetcode.com/problems/product-of-array-except-self/
#
# Given an array of n integers where n > 1, nums,
# return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
#
# Solve it without division and in O(n).
#
# For example, given [1,2,3,4], return [24,12,8,6].
#
# Follow up:
# Could you solve it with constant space complexity?
# (Note: The output array does not count as extra space for the purpose of space complexity analysis.)

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        product = 1
        zero_cnt = 0
        for i in nums:
            if i == 0:
                zero_cnt = zero_cnt + 1
                if zero_cnt == 2:
                    return [0] * len(nums)
                zero_idx = nums.index(i)
                continue
            product = product * i

        # only one zero exists
        if zero_cnt == 1:
            output = [0] * len(nums)
            output[zero_idx] = product
            return output

        # no zero exists
        output = [product / i for i in nums]
        return output
