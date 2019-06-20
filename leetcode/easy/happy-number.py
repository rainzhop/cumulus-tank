# https://leetcode.com/problems/happy-number/
#
# Write an algorithm to determine if a number is "happy".
#
# A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the sum of the squares of its digits,
# and repeat the process until the number equals 1 (where it will stay),
# or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy numbers.
#
# Example: 19 is a happy number
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
#
# Credits:
# Special thanks to @mithmatt and @ts for adding this problem and creating all test cases.

class Solution(object):
    def __init__(self):
        self.past = []
        
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        if n in self.past:
            return False
        self.past.append(n)
        d = []
        while n != 0:
            d.append(n % 10)
            n = n / 10
        s = 0
        for i in d:
            s += i ** 2
        return self.isHappy(s)
