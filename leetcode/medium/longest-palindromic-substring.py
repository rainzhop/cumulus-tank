# https://leetcode.com/problems/longest-palindromic-substring/
#
# Given a string S, find the longest palindromic substring in S.
# You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == '':
            return ''
        longestSize = 0
        longestPalindrome = ''
        i = 0
        while i < len(s) - 1:
            palindrome, size = self.findPalindrome(s, i)
            print palindrome, size
            if size > longestSize:
                longestSize = size
                longestPalindrome = palindrome
            i = i + 1
        if longestSize <= 1:
            return s[-1]
        return longestPalindrome


    def findPalindrome(self, s, i):
        ibak = i
        j = i + 1
        while i >= 0 and j < len(s):
            if s[i] != s[j]:
                break
            i, j = i - 1, j + 1
        even_pal, even_size = s[i + 1:j], j - i - 1

        i = ibak
        j = i + 1
        if s[i] != s[j]:
            i = i - 1
        while i >= 0 and j < len(s):
            if s[i] != s[j]:
                break
            i, j = i - 1, j + 1
        odd_pal, odd_size = s[i + 1:j], j - i - 1

        return (even_pal, even_size) if even_size > odd_size else (odd_pal, odd_size)
