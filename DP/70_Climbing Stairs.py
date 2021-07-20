'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''


class Solution:
    #method 1. DP. O(n), S(n)
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        S = [1, 2]
        for i in range(2, n):
            S.append(S[i - 1] + S[i - 2])
        res = S[n - 1]
        return res
