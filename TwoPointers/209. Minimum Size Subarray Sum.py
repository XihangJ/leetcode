'''
Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
'''

class Solution:
    # method 1. O(n), S(1)
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        min_len = inf
        curr = nums[0]
        while right < len(nums):
            if curr >= target:
                min_len = min(min_len, right - left + 1)
                if left == right:
                    left += 1
                    right += 1
                    if right < len(nums): curr = nums[right]
                else:
                    curr -= nums[left]
                    left += 1
            else:
                right += 1
                if right < len(nums): curr += nums[right]
        if min_len == inf: return 0
        return min_len
