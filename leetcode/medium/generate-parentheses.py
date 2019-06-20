# https://leetcode.com/problems/generate-parentheses/
#
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
# For example, given n = 3, a solution set is:
#
# "((()))", "(()())", "(())()", "()(())", "()()()"

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret = []
        stack = ['(']
        while stack != []:
            s = stack.pop()
            if len(s) == n * 2:
                if self.isOk(s):
                    ret.append(s)
            else:
                stack.append(s + ')')
                stack.append(s + '(')

    def isOk(self, s):
        cnt = 0
        for i in s:
            if i == '(': cnt += 1
            elif i == ')': cnt -= 1
            if cnt < 0: return False
        if cnt == 0:
            return True








if __name__ == '__main__':
    s = Solution()
    print s.generateParenthesis(3)
