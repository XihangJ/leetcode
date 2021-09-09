'''
Given a pattern and a string s, return true if s matches the pattern.

A string s matches a pattern if there is some bijective mapping of single characters to strings such that if each character in pattern is replaced by the string it maps to, then the resulting string is s. A bijective mapping means that no two characters map to the same string, and no character maps to two different strings.
'''

class Solution:
    #method. Backtracking. ?? O(n!), S(n) ??
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        
        def backtrack(pattern, i, s, j, pattern_map, s_set):
            
            if i == len(pattern) and j == len(s): return True
            elif i == len(pattern) or j == len(s): return False
            
            if pattern[i] in pattern_map:
                curr_s = pattern_map[pattern[i]]
                if (j + len(curr_s) > len(s)) or (curr_s != s[j : j + len(curr_s)]):
                    return False    
                return backtrack(pattern, i + 1, s, j + len(curr_s), pattern_map, s_set)
            
            else:
                for end in range(j + 1, len(s) + 1):
                    curr_s = s[j : end]
                    if curr_s in s_set: continue
                    pattern_map[pattern[i]] = curr_s
                    s_set.add(curr_s)
                    if backtrack(pattern, i + 1, s, end, pattern_map, s_set): return True
                    
                    pattern_map.pop(pattern[i])
                    s_set.remove(curr_s)
            return False
        
        pattern_map = {}
        s_set = set()
        return backtrack(pattern, 0, s, 0, pattern_map, s_set)
