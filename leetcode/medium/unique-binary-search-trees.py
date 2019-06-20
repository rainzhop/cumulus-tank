# https://leetcode.com/problems/unique-binary-search-trees/
#
# Given n, how many structurally unique BST's (binary search trees) that store values 1...n?
#
# For example,
# Given n = 3, there are a total of 5 unique BST's.
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # ---- Time Exceed ----
        # if n == 0:
        #     return 1
        # if n == 1:
        #     return 1
        # count = 2 * self.numTrees(n - 1)
        # for i in range(2, n):
        #     count = count + self.numTrees(i - 1) * self.numTrees(n - i)
        # ---- Time Exceed ----

        count = [0] * (n + 1)
        count[0] = 1
        count[1] = 1
        for i in xrange(2, n + 1):
            count[i] = 2 * count[i - 1]
            for j in xrange(2, i):
                count[i] = count[i] + count[j - 1] * count[i - j]
        return count[n]
