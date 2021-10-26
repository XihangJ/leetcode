'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
'''

class Solution:
    #DP. O(N), S(1)
    #find the max of A[0..n-1] and A[1..n]
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums)
        if len(nums) == 3: return max(nums[0], nums[2], nums[1])
        
        
        def houseRob(start, end):
            curr = 0
            prev = 0
            for i in range(start, end + 1):
                curr, prev = max(nums[i] + prev, curr), curr
            return curr
            
        return max(houseRob(0, len(nums) - 2), houseRob(1, len(nums) - 1))
