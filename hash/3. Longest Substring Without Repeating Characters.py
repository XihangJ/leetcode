'''
Given a string s, find the length of the longest substring without repeating characters.
'''

class Solution:
    #method 1. Hashmap + greedy. O(n), S(n)
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        d = {}
        max_length = 0
        curr_length = 0
        index_start = 0
        for i in range(len(s)):
            if s[i] not in d:
                curr_length = i - index_start + 1
                d[s[i]] = i
                max_length = max(max_length, curr_length)
            else:
                index_start = max(d[s[i]] + 1, index_start) # important! To decide what is the new start index
                curr_length = i - index_start + 1
                d[s[i]] = i
                max_length = max(max_length, curr_length)
        return max_length
