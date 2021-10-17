'''
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
'''

class Solution:
    
    #method 2. BFS. O(N), S(1)
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return 0
        if n > 1 and nums[0] == 0: return -1
        
        jumps = 0
        start, end = 0, 0
        reach_max = nums[0]
        
        while start <= end and end < n:
            jumps += 1
            for j in range(start, end + 1):
                if j > reach_max: return -1  # can not reach the the end
                reach_max = max(nums[j] + j, reach_max)
            if reach_max >= n - 1: return jumps
            start = end + 1
            end = reach_max
        return -1
                
        
        
    '''
    #method 1. DP. O(n ** 2), S(1)
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        n = len(nums)
        nums[-1] = 0
        for i in range(n - 2, -1, -1):
            min_step = inf
            right_bound = min(i + nums[i] + 1, n)
            for j in range(i + 1, right_bound):
                min_step = min(min_step, nums[j] + 1)
            nums[i] = min_step
        print(nums)
        return nums[0]
    '''
