# https://leetcode.com/problems/permutations/
#
# Given a collection of numbers, return all possible permutations.
#
# For example,
# [1,2,3] have the following permutations:
# [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        if len(nums) == 1:
            return [nums]
        for i in xrange(len(nums)):
            tmp = nums[:]
            pick = tmp[i]
            del tmp[i]
            less = self.permute(tmp)
            for j in less:
                j.insert(0, pick)
            ret.extend(less)
        return ret


if __name__ == '__main__':
    s = Solution()
    print s.permute(range(0,6))
