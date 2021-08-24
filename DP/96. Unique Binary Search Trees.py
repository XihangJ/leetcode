'''
Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.
'''
class Solution:
    #method 1. DP. O(n ^ 2), S(n)
    def numTrees(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        dp_arr = [1, 1, 2]
        for num in range(3, n + 1):
            curr = 0
            for i in range(num):
                curr += dp_arr[i] * dp_arr[num - i - 1]
            dp_arr.append(curr)
        return dp_arr[-1]
