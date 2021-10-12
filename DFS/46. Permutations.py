'''
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
'''

class Solution:
    #Backtracking. O(n!), S(n)
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(start):
            if start == len(nums) - 1:
                res.append(nums.copy())
                return
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[i], nums[start] = nums[start], nums[i]
            
        res = []
        backtrack(0)
        return res
