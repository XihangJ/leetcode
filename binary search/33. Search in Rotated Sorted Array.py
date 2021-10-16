'''
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
'''

class Solution:
    #method: binary search. O(logn), S(1)
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1
        if len(nums) == 1:
            if nums[0] == target: return 0
            else: return -1
        n = len(nums)
        left, right = 0, n - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] == target: return mid
            if nums[left] == target: return left
            if nums[right] == target: return right
            elif nums[mid] < nums[left]:
                if (target < nums[mid]) or (target > nums[left]):
                    right = mid
                else:
                    left = mid
            elif nums[mid] >= nums[left]:
                if (target > nums[mid]) or (target < nums[left]):
                    left = mid
                else:
                    right = mid
        
        if nums[left] == target: return left
        elif nums[right] == target: return right
        else: return -1
