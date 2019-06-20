# https://leetcode.com/problems/palindrome-number/
#
# Determine whether an integer is a palindrome. Do this without extra space.
#
# Some hints:
# Could negative integers be palindromes? (ie, -1)
#
# If you are thinking of converting the integer to string, note the restriction of using extra space.
#
# You could also try reversing an integer. However, if you have solved the problem "Reverse Integer",
# you know that the reversed integer might overflow. How would you handle such case?
#
# There is a more generic way of solving this problem.

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x == 0:
            return True

        n = 0
        while x / (10**n) != 0:
            n = n + 1

        left = n - 1
        right = 0

        if left == right:
            return True

        while True:
            if x / (10**left) % 10 != x / (10**right) % 10:
                return False
            if left - right == 1 or left == right:
                return True
            left, right = left - 1, right + 1


if __name__ == '__main__':
    s = Solution()
    print s.isPalindrome(12321)
