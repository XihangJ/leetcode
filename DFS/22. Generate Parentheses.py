'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
'''

class Solution:
    #method2. backtracking. O(catlan number) - O(4^n / n*sqrt(n)), S(4^n / n*sqrt(n))
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        
        def backtracking(curr, num_open, num_close):
            if len(curr) == 2 * n:
                res.append(''.join(curr))
            if num_open > 0:
                curr.append('(')
                backtracking(curr, num_open - 1, num_close)
                curr.pop()
            if num_close > num_open:
                curr.append(')')
                backtracking(curr, num_open, num_close - 1)
                curr.pop()
        backtracking([], n, n)
        return res
    
    
    '''
    #method1. DP. O(n ** 2), S(n ** 2). Onbbbbbbbbbbbbly Get count!!
    def generateParenthesis(self, n: int) -> List[str]:
        C = [[0 for i in range(n + 1)] for j in range(n + 1)]
        for i in range(1, n + 1):
            C[i][0] = 1
        for j in range(1, n + 1):
            for i in range(j, n + 1):
                if i == j:
                    C[i][j] = C[i][j - 1]
                else:
                    C[i][j] = C[i][j - 1] + C[i - 1][j]
        res = C[n][n]
        return res
    '''
