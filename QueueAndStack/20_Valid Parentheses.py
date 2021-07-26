'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
'''


class Solution:
    #method 1. stack. O(n), S(n)
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if not stack: stack.append(s[i])
            elif ((stack[-1] == '(' and s[i] == ')') or
                  (stack[-1] == '[' and s[i] == ']') or
                  (stack[-1] == '{' and s[i] == '}')):
                stack.pop()
            else:
                stack.append(s[i])
        if stack: return False
        else: return True
