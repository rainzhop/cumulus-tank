# https://leetcode.com/problems/integer-to-roman/
#
# Given an integer, convert it to a roman numeral.
#
# Input is guaranteed to be within the range from 1 to 3999.

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ret = ""
        ret = ret + "M" * (num / 1000)
        num = num % 1000
        ret = ret + "CM" * (num / 900)
        num = num % 900
        ret = ret + "D" * (num / 500)
        num = num % 500
        ret = ret + "CD" * (num / 400)
        num = num % 400
        ret = ret + "C" * (num / 100)
        num = num % 100
        ret = ret + "XC" * (num / 90)
        num = num % 90
        ret = ret + "L" * (num / 50)
        num = num % 50
        ret = ret + "XL" * (num / 40)
        num = num % 40
        ret = ret + "X" * (num / 10)
        num = num % 10
        ret = ret + "IX" * (num / 9)
        num = num % 9
        ret = ret + "V" * (num / 5)
        num = num % 5
        ret = ret + "IV" * (num / 4)
        num = num % 4
        ret = ret + "I" * (num / 1)
        return ret
