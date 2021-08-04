'''
Given a string s of '(' , ')' and lowercase English characters. 

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
'''

class Solution:
    #method 1. Using 1 stack and 1 set. O(n), S(n)
    def minRemoveToMakeValid(self, s: str) -> str:
        if not s: return True
        stack = []
        set_removal = set()
        #find indeces
        for i in range(len(s)):
            digit = s[i]
            if digit != '(' and digit != ')': continue
            elif digit == '(':
                stack.append(i)
            elif digit == ')':
                if not stack: set_removal.add(i)
                else: stack.pop()
        #build str
        res_list = []
        index = 0
        for i in range(len(s)):
            if i in set_removal: continue
            elif index < len(stack):
                if i != stack[index]: res_list.append(s[i])
                else: index += 1
            else: res_list.append(s[i])
        res = ''.join(res_list)
        return res
