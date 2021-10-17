'''
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
'''

class Solution:
    #O(n), S(1)
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True
        if len(nums) > 1 and nums[0] == 0: return False
        n = len(nums)
        reach_max = 0
        for i in range(n):
            if i <= reach_max:
                reach_max = max(nums[i] + i, reach_max)
        return reach_max >= n - 1
