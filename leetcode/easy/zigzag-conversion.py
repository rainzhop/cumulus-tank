# https://leetcode.com/problems/zigzag-conversion/
#
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
# (you may want to display this pattern in a fixed font for better legibility)
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string text, int nRows);
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        rowList = []
        for i in range(numRows):
            rowList.append([])

        i = 0
        direction = 0 # 0:down, 1:up
        for c in s:
            rowList[i].append(c)
            i = (i + 1) if direction == 0 else (i - 1)
            if i == 0:
                direction = 0
            elif i == numRows - 1:
                direction = 1

        ret_s = ''
        for row in rowList:
            ret_s = ret_s + ''.join(row)

        return ret_s

if __name__ == '__main__':
    s = Solution()
    print s.convert("ABCEDFG", 1)
