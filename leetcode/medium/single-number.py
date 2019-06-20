# https://leetcode.com/problems/single-number/
#
# Given an array of integers, every element appears twice except for one. Find that single one.
#
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(0, len(nums), 2):
            try:
                if nums[i] != nums[i + 1]:
                    return nums[i]
            except:
                return nums[i]
        return None

if __name__ == "__main__":
    nums = [3,4,2,3,4,5,5]
    s = Solution()
    print s.singleNumber(nums)
