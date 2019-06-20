# https://leetcode.com/problems/search-a-2d-matrix/
#
# Write an efficient algorithm that searches for a value in an m x n matrix.
# This matrix has the following properties:
#
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
#
# For example,
# Consider the following matrix:
# [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# Given target = 3, return true.

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        left, right = 0, m - 1
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        while left != right:
            mid = (left + right) / 2
            if target < matrix[mid][-1]:
                right = mid
            else:
                left = mid + 1
        if target in matrix[left]:
            return True
        else:
            return False
