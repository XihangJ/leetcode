'''
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
'''

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(start, curr):
            res.append(curr.copy())
            for i in range(start, len(nums)):
                # important!! 
                #1) i > 0: make sure that i - 1 >= 0
                #2) i > start: make sure that in the same level, no repeated is included
                if i > start and nums[i - 1] == nums[i]: continue 
                curr.append(nums[i])
                backtrack(i + 1, curr)
                curr.pop()
            return
        nums.sort()
        res = []
        backtrack(0, [])
        return res
