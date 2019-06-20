# https://leetcode.com/problems/maximum-subarray/
#
# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
#
# For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
# the contiguous subarray [4,−1,2,1] has the largest sum = 6.
#
# More practice:
# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        subArrSum = ret = -(2**32)
        for i in nums:
            subArrSum = i if subArrSum < 0 else subArrSum + i
            if subArrSum > ret: ret = subArrSum
        return ret
