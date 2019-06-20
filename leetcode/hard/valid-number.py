# https://leetcode.com/problems/valid-number/
# 
# Validate if a given string is numeric.
# 
# Some examples:
#     "0" => true
#     " 0.1 " => true
#     "abc" => false
#     "1 a" => false
#     "2e10" => true
# 
# Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.
# 
# Update (2015-02-10):
# The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button to reset your code definition.

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        digits = '0123456789'
        e_cnt = 0
        dot_cnt = 0
        s = s.strip()
        if s == "":
            return False
        for i in xrange(len(s)):
            print i
            if s[i] in digits:
                continue
            elif s[i] == '+' or s[i] == '-':
                if i == 0:
                    continue
                elif s[i - 1] == 'e':
                    continue
                return False
            elif s[i] == 'e':
                e_cnt += 1
                if e_cnt > 1:
                    return False
                if i == 0 or i == len(s) - 1:
                    return False
                if s[i - 1] not in digits and s[i - 1] != '.' and s[i - 1] != '+' and s[i - 1] != '-':
                    return False
                if s[i + 1] not in digits:
                    return False
            elif s[i] == '.':
                dot_cnt += 1
                if dot_cnt > 1:
                    return False
                if s[i - 1] not in digits:
                    return False
                if i == 0:
                    if s[i + 1] == 'e':
                        return False
                if i != len(s) - 1:
                    if s[i + 1] not in digits and s[i + 1] != 'e':
                        return False
            else:
                return False
        return True

s = Solution()
print s.isNumber('+123.e-1')
