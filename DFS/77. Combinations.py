'''
Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

You may return the answer in any order.

 

Example 1:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''

class Solution:
    #method 1. Backtracking. O(n!/(n-k)!/k!), S(k)
    def __init__(self):
        self.res = []

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.backtrack(n, k, [], [], 1)
        return self.res
    
    def backtrack(self, n, k, curr, res, start):
        if len(curr) == k:
            self.res.append(curr.copy())
            return
        if k - len(curr) > n - start + 1: return #!! saves a lot of time
        for num in range(start, n + 1):
            curr.append(num)
            self.backtrack(n, k, curr, res, num + 1)
            curr.pop()
