'''
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
'''

class Solution:
    #method 1. 2 pointers. O(n), S(n)
    def minWindow(self, s: str, t: str) -> str:
        n, m = len(s), len(t)
        if n < m: return ''
        
        d_t = {}
        for ch in t:
            if ch not in d_t: d_t[ch] = 1
            else: 
                d_t[ch] += 1
                
        s_t = set()
        for key in d_t: s_t.add(key)
        
        left, right = 0, 0
        res_left, res_right = None, None
        min_len = inf
        while left <= right and right < n:
            front = s[right]
            if front in d_t:
                d_t[front] -= 1
                if d_t[front] == 0:
                    s_t.remove(front)
            while len(s_t) == 0:
                if right - left + 1 < min_len:
                    res_left, res_right = left, right
                min_len = min(min_len, right - left + 1)
                if s[left] in d_t:
                    d_t[s[left]] += 1
                    if d_t[s[left]] == 1:
                        s_t.add(s[left])
                left += 1  
            right += 1
        if res_left != None and res_right != None:
            return ''.join(s[res_left : res_right + 1])
        else:
            return ''
