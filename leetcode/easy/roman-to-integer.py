# https://leetcode.com/problems/roman-to-integer/
#
# Given a roman numeral, convert it to an integer.
#
# Input is guaranteed to be within the range from 1 to 3999.

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        last_c = None
        th = 0
        h = 0
        t = 0
        d = 0
        for c in s.upper():
            if c == 'M':
                # 1000-3000, C+s: 900
                if last_c == 'C':
                    h = 9
                else:
                    th = th + 1
            if c == 'D':
                # 500-800, C+s: 400
                if last_c == 'C':
                    h = 4
                else:
                    h = 5
            if c == 'C':
                # 100-300, X+s: 90
                if last_c == 'X':
                    t = 9
                else:
                    h = h + 1
            if c == 'L':
                # 50-80, X+s: 40
                if last_c == 'X':
                    t = 4
                else:
                    t = 5
            if c == 'X':
                # 10-30, I+s: 9
                if last_c == 'I':
                    d = 9
                else:
                    t = t + 1
            if c == 'V':
                # 5-8, I+s: 4
                if last_c == 'I':
                    d = 4
                else:
                    d = 5
            if c == 'I':
                # 1-3
                d = d + 1
            last_c = c
        ret = th*1000 + h*100 + t*10 + d
        return ret

if __name__ == '__main__':
    s = Solution()
    print s.romanToInt("DCXXI")
