# https://leetcode.com/problems/minimum-path-sum/
#
# Given a m x n grid filled with non-negative numbers,
# find a path from top left to bottom right which minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        ret = [[0] * n] * m
        for i in xrange(0, m):
            for j in xrange(0, n):
                h = 0 if i == 0 else ret[i - 1][j]
                v = 0 if j == 0 else ret[i][j - 1]
                ret[i][j] = min(h, v) + grid[i][j]
        return ret[m - 1][n - 1]
