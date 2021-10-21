'''
Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

Example 1:

Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
'''

class Solution:
    #method 1. sliding window. O(n), S(1)
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res = 0
        left, right = 0, 0
        curr = nums[0]
        while right < len(nums):
            if curr < k: 
                res += right - left + 1
                right += 1
                if right < len(nums): curr *= nums[right]
            else:
                if left == right:
                    left += 1
                    right += 1
                    if right < len(nums): curr = nums[right]
                else:
                    curr /= nums[left]
                    left += 1
        return res
            
