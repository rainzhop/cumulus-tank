# https://leetcode.com/problems/reverse-integer/
#
# Reverse digits of an integer.
#
# Example1: x = 123, return 321
# Example2: x = -123, return -321
#
# Have you thought about this?
# Here are some good questions to ask before coding.
# Bonus points for you if you have already thought through this!
#
# If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.
#
# Did you notice that the reversed integer might overflow?
# Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. How should you handle such cases?
#
# For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
#
# Update (2014-11-10):
# Test cases had been added to test the overflow behavior.

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        sign = -1 if x < 0 else 1
        digits = list(str(abs(x)))
        digits.reverse()
        while digits[0] == '0':
            digits.remove('0')
        y = eval(''.join(digits))
        y = sign * y
        if y >= 2**31 - 1 or y < -(2**31 - 1):
            return 0
        return y

if __name__ == '__main__':
    s = Solution()
    print s.reverse(900000)
