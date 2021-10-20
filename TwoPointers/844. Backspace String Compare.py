'''
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.
'''

class Solution:
    
    
    # method 2. using stack
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        for ch in s:
            if ch != '#':
                stack_s.append(ch)
            elif stack_s:
                stack_s.pop()

        stack_t = []
        for ch in t:
            if ch != '#':
                stack_t.append(ch)
            elif stack_t:
                stack_t.pop()
                
        return stack_s == stack_t
    
    '''
    # method 1. 2 pointers from the end of s and t. O(n), S(1)
    def backspaceCompare(self, s: str, t: str) -> bool:
        i_s = len(s) - 1
        i_t = len(t) - 1
        while i_s >= 0 and i_t >= 0:
            count_back = 0
            while i_s >= 0 and (s[i_s] == '#' or count_back > 0):
                if s[i_s] == '#': count_back += 1
                else: count_back -= 1
                i_s -= 1
            count_back = 0
            while i_t >= 0 and (t[i_t] == '#' or count_back > 0):
                if t[i_t] == '#': count_back += 1
                else: count_back -= 1
                i_t -= 1   
            if i_s < 0 and i_t < 0: return True
            elif i_s >= 0 and i_t >= 0 and s[i_s] != t[i_t]: return False
            elif i_s < 0 or i_t < 0: break
            i_s -= 1
            i_t -= 1
           
        if i_s < 0 and i_t < 0: return True
        elif i_s >= 0:
            count_back = 0
            while i_s >= 0 and (s[i_s] == '#' or count_back > 0):
                if s[i_s] == '#': count_back += 1
                else: count_back -= 1
                i_s -= 1
            return i_s < 0
        elif i_t >= 0:
            count_back = 0
            while i_t >= 0 and (t[i_t] == '#' or count_back > 0):
                if t[i_t] == '#': count_back += 1
                else: count_back -= 1
                i_t -= 1
            return i_t < 0
            
    '''
