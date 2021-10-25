'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
'''

class Solution:
    # O(N * 4 ** N), S(N)
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        buttons = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'],
                  '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'],
                  '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        
        def backtrack(start, curr):
            if len(curr) == len(digits):
                res.append(''.join(curr))
                return
            d = digits[start]
            for ch in buttons[d]:
                curr.append(ch)
                backtrack(start + 1, curr)
                curr.pop()
            
        res = []
        backtrack(0, [])
        return res
