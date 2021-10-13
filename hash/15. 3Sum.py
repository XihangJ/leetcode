'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
'''

class Solution:
    
    #method 1. sort + 2 pointers. O(n ** 2), S(logn) --> depends on what sorting algo
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3: return []
        nums.sort()
        num = None
        res = []
        
        for i in range(len(nums) - 2):
            if nums[i] == num: continue
            num = nums[i]
            curr = self.twoSum(nums, i + 1, len(nums) - 1, -nums[i])
            if curr: 
                for l in curr:
                    res.append([nums[i], l[0], l[1]])
        return res
            
            
    def twoSum(self, nums, left, right, target):
        res = []
        while left < right:
            num_left, num_right = nums[left], nums[right]
            if nums[left] + nums[right] == target:
                res.append([nums[left], nums[right]])
                while left < len(nums) and nums[left] == num_left: left += 1
                while right >= 0 and nums[right] == num_right: right -= 1
            elif nums[left] + nums[right] < target:
                while left < len(nums) and nums[left] == num_left: left += 1
            else:
                while right >= 0 and nums[right] == num_right: right -= 1
        return res
    
    '''
    #method 1. hashmap + single pass scan. O(n ** 2), S(n)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        res = []
        for i in range(len(nums)):
            curr = self.twoSum(nums, i + 1, -nums[i])
            if curr:
                for tmp in curr:
                    res_tmp = [nums[i]] + tmp
                    res_tmp.sort()
                    if res_tmp not in res:
                        res.append(res_tmp.copy())           
        return res
        
    def twoSum(self, nums, startIndex, target):
        d=set()
        res = []
        for i in range(startIndex, len(nums)):
            num = nums[i]
            curr = target - num
            if num in d:
                if [curr, num] not in res and [num, curr] not in res:
                    res.append([curr, num])
            d.add(curr)
        return res
        '''
