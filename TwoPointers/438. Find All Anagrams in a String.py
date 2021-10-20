'''
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''

class Solution:
    #method 1. sliding window + hashtable + hashset. O(m + n), s(n)
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p): return []
        d_p, s_p = {}, set()
        for ch in p:
            if ch in d_p:
                d_p[ch] += 1
            else:
                d_p[ch] = 1
                s_p.add(ch)
        res = []
        left, right = 0, len(p) - 1
        for i in range(right + 1):
            if s[i] in d_p: 
                d_p[s[i]] -= 1
                if d_p[s[i]] == 0: s_p.remove(s[i])
            if len(s_p) == 0: res.append(left)   
        while right < len(s) - 1:
            if s[left] in d_p: 
                d_p[s[left]] += 1
                if d_p[s[left]] == 1: s_p.add(s[left])
            
            if s[right + 1] in d_p: 
                d_p[s[right + 1]] -= 1
                if d_p[s[right + 1]] == 0 and s[right + 1] in s_p: s_p.remove(s[right + 1])
            
            if len(s_p) == 0: res.append(left + 1)
                
            left += 1
            right += 1
        
        return res
