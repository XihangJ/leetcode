'''
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        #method 3. bitmask
        n = len(nums)
        nth_bit = 2**n
        res = []
        for i in range(2**n):
            bitmask = bin(i | nth_bit)[3:]
            subset_tmp = [nums[j] for j in range(n) if bitmask[j] == '1']
            res.append(subset_tmp)
        return res
        
        
        
        '''
        #method 2.2 backtracking without length
        def dfs(start, curr):
            res.append(curr.copy())
            for i in range(start, len(nums)):
                curr.append(nums[i])
                dfs(i + 1, curr)
                curr.pop()
            return
        res = []
        dfs(0, [])
        return res
        '''
        
        
        '''
        #method 2.1 backtracking
        def backtrack(start, curr, length):
            
            if len(curr) == length:
                results.append(curr.copy())# Attention! Must be deep copy here.
                return
            for i in range(start, len(nums)):
                curr.append(nums[i])
                backtrack(i + 1, curr, length)
                curr.pop()
        results = []
        for length in range(len(nums) + 1):
            backtrack(0, [], length)
        return results
        '''
        
        '''
        #method 1. cascading
        results = [[]]
        for num in nums:
            results += [result + [num] for result in results]
        return results
        '''
        
