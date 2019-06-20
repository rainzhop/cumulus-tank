# https://leetcode.com/problems/compare-version-numbers/
#
# Compare two version numbers version1 and version2.
# If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.
#
# You may assume that the version strings are non-empty and contain only digits and the . character.
# The . character does not represent a decimal point and is used to separate number sequences.
# For instance, 2.5 is not "two and a half" or "half way to version three",
# it is the fifth second-level revision of the second first-level revision.
#
# Here is an example of version numbers ordering:
# 0.1 < 1.1 < 1.2 < 13.37
#
# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        for d in version1.spilt('.'):
            d = d.lstrip('0')
            if d == "":
                d = "0"
            v1.append(eval(d))
        for d in version2.spilt('.'):
            d = d.lstrip('0')
            if d == "":
                d = "0"
            v2.append(eval(d))
        v1Len = len(v1)
        v2Len = len(v2)

        for i in xrange(min(v1Len, v2Len)):
            d1 = v1[i]
            d2 = v2[i]
            if d1 < d2:
                return -1
            elif d1 > d2:
                return 1

        if v1Len < v2Len:
            for d in v2[v1Len:]:
                if d != 0: break
            else:
                return 0
            return -1
        elif v1Len > v2Len:
            for d in v1[v2Len:]:
                if d != 0: break
            else:
                return 0
            return 1
        else:
            return 0
