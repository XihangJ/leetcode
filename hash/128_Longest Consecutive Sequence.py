'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
'''

class Solution:
    
    #method 2. hashset. iterate items in hashset
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        s = set(nums)
        count = 1
        res = 1
        for num in s:
            count = 1
            if num - 1 not in s: 
                while num + 1 in s:
                    count += 1
                    num += 1
                res = max(res, count)
        return res
    
    
    
    '''
    #method 1. hashset. bucket-like count. Time Limit Exceeded
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        s = set()
        num_max, num_min = -inf, inf
        for num in nums:
            s.add(num)
            num_max = max(num_max, num)
            num_min = min(num_min, num)
        
        count = 0
        res = 1
        for i in range(num_min, num_max + 1):
            if i in s: 
                count += 1
            else: count = 0
            res = max(res, count)
        return res
        '''
