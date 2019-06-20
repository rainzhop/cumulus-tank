# https://leetcode.com/problems/number-of-islands/
#
# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.
#
# Example 1:
# 11110
# 11010
# 11000
# 00000
# Answer: 1
#
# Example 2:
# 11000
# 11000
# 00100
# 00011
# Answer: 3
#
# Credits:
# Special thanks to @mithmatt for adding this problem and creating all test cases.

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        grid = [[int(j) for j in i] for i in grid]
        if grid == [] or grid == [[]]:
            return 0
        gridLen = len(grid)
        rowLen = len(grid[0])
        def color(i, j):
            if i < 0 or j < 0 or i > gridLen - 1 or j > rowLen - 1:
                return
            if grid[i][j] != 1:
                return
            grid[i][j] = 2
            color(i, j + 1)
            color(i + 1, j)
            color(i - 1, j)
            color(i, j - 1)
        count = 0
        for i in xrange(gridLen):
            for j in xrange(rowLen):
                if grid[i][j] == 1:
                    color(i, j)
                    count += 1
        return count
