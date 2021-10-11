'''
You are given a license key represented as a string s that consists of only alphanumeric characters and dashes. The string is separated into n + 1 groups by n dashes. You are also given an integer k.

We want to reformat the string s such that each group contains exactly k characters, except for the first group, which could be shorter than k but still must contain at least one character. Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.

Return the reformatted license key.
'''

class Solution:
    #method 1. Naive iteration. O(n), S(n)
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s_list = []
        for ch in s:
            if ch != '-':
                s_list.append(ch.upper())
        if k >= len(s_list): return ''.join(s_list)
        
        first_len = len(s_list) % k
        number_parts = len(s_list) // k + (1 * (first_len > 0))
        if first_len == 0: first_len = k
        
        res = []
        for i in range(first_len):
            res.append(s_list[i])
        res.append('-')
        
        count = 0
        for i in range(first_len, len(s_list)):
            if count == k:
                res.append('-')
                count = 0
            res.append(s_list[i])
            count += 1
        
        return ''.join(res)
