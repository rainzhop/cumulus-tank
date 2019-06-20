# https://leetcode.com/problems/rotate-image/
#
# You are given an n x n 2D matrix representing an image.
#
# Rotate the image by 90 degrees (clockwise).
#
# Follow up:
# Could you do this in-place?

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in xrange(0, n / 2):
            for j in xrange(i, n - i)
            last = matrix[i][j]
            for time in xrange(4):
                print i, j
                current = matrix[j][n - i - 1]
                matrix[j][n - i - 1] = last
                i, j = j, n - i - 1
                last = current
        return
