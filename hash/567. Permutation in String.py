'''
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.
'''

class Solution:
    # Using hashmap. 2 scan. O(m + n), S(m) <-- len(s1) = m
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        
        d = {}
        for ch in s1:
            if ch not in d: 
                d[ch] = 1
            else: 
                d[ch] += 1
        
        remain = len(d)
        for i in range(len(s1)):
            if s2[i] in d: 
                d[s2[i]] -= 1
                if d[s2[i]] == 0: remain -= 1
                if remain == 0: return True        

        for i in range(len(s1), len(s2)):
            start = i - len(s1)
            if s2[start] in d: 
                d[s2[start]] += 1
                if d[s2[start]] == 1: remain += 1 #important! only when a ch from 0 to 1 increase the remain
            if s2[i] in d: 
                d[s2[i]] -= 1
                if d[s2[i]] == 0: remain -= 1
                if remain == 0: return True

        return False    
                    
