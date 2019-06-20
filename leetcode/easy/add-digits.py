# https://leetcode.com/problems/add-digits/
#
# Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
#
# For example:
# Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.
#
# Follow up:
# Could you do it without any loop/recursion in O(1) runtime?
#
# Hint:
# 1.A naive implementation of the above process is trivial. Could you come up with other methods?
# 2.What are all the possible results?
# 3.How do they occur, periodically or randomly?
# 4.You may find this Wikipedia(https://en.wikipedia.org/wiki/Digital_root) article useful.
#
# Credits:
# Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        ret = 0
        while num != 0:
            ret = ret + num % 10
            num = num / 10
        if ret < 10:
            return ret
        else:
            return self.addDigits(ret)

if __name__ == '__main__':
    s = Solution()
    print s.addDigits(4587)
