# https://leetcode.com/problems/longest-substring-without-repeating-characters/
#
# Given a string, find the length of the longest substring without repeating characters.
# For example, the longest substring without repeating letters for "abcabcbb" is "abc",
# which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = []
        max_len = 0
        i = 0
        j = 0
        while j < len(s):
            if s[j] not in longest:
                longest.append(s[j])
                j = j + 1
            else:
                if max_len < len(longest):
                    max_len = len(longest)
                idx = longest.index(s[j]) + 1
                longest = longest[idx:]
                longest.append(s[j])
                i = i + idx
                j = j + 1
                continue
        if max_len < len(longest):
            max_len = len(longest)
        return max_len
