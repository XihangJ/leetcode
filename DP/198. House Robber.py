'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
'''

class Solution:
    #method: DP. O(n), S(n)
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums)
        if len(nums) == 3: return max(nums[0] + nums[2], nums[1])
        money = [nums[0], nums[1], nums[0] + nums[2]]
        for i in range(3, len(nums)):
            money.append(nums[i] + max(money[i - 3], money[i - 2]))
        return max(money[-1], money[-2])
