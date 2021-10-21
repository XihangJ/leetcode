'''
Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
'''

class Solution:
    
    
    #method 2. Binary Search. O(nlogn), S(n)
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefix = []
        curr = 0
        for num in nums:
            curr += num
            prefix.append(curr)
        min_len = inf
        for i in range(len(nums)):
            end = self.searchRight(prefix, nums, i, len(nums) - 1, target)
            if end == -1: break
            min_len = min(min_len, end - i + 1)
        if min_len != inf: return min_len
        return 0
    
    def searchRight(self, prefix, nums, left, right, target):
        start = left
        end = right
        while start + 1 < end:
            mid = start + (end - start) // 2
            if prefix[mid] - prefix[left] + nums[left] > target:
                end = mid
            elif prefix[mid] - prefix[left] + nums[left] < target:
                start = mid
            else:
                return mid
        if prefix[start] - prefix[left] + nums[left] >= target: return start
        if prefix[end] - prefix[left] + nums[left] >= target: return end
        return -1
     
    '''
    # method 1. 2 pointers. O(n), S(1)
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
    '''
