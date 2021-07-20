'''
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.
'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        
        #method 4: quick select. O(N) avg. O(N^2) worst. S(1) 
        if nums == []:
            return

        def quickSelect(nums, left, right, k):
            if left == right:
                return nums[left]
            pivot = nums[(left + right) // 2]
            left_index, right_index = left, right
            while left_index <= right_index:
                while left_index <= right_index and nums[left_index] > pivot: #kth maximum
                    left_index += 1
                while left_index <= right_index and nums[right_index] < pivot:
                    right_index -= 1
                if left_index <= right_index:
                    nums[left_index], nums[right_index] = nums[right_index], nums[left_index]
                    left_index += 1
                    right_index -= 1
            if right_index - left >= k - 1:
                return quickSelect(nums, left, right_index, k)
            elif left_index - left <= k - 1:
                return quickSelect(nums, left_index, right, k - left_index + left)
            else:
                return nums[right_index + 1]
        return quickSelect(nums, 0, len(nums) - 1, k)
        
        '''
        #method 3: Partial heapsort O(N + klogN), S(N). Can be in place.
        import heapq
        pq = []
        for i in range(len(nums)):
            heapq.heappush(pq, - nums[i])
        for i in range(k - 1):
            heapq.heappop(pq)
        return - heapq.heappop(pq)
        '''
        
        '''
        #method 2: Online selection. O(Nlogk), S(k)
        import heapq
        pq = nums[:k]
        heapq.heapify(pq)
        for i in range(k, len(nums)):
            heapq.heappush(pq, nums[i])
            heapq.heappop(pq)
        return pq[0]
        '''    
        
        '''
        #method 1: partial selection sort. O(kN), not good enough
        for i in range(k):
            max_temp = nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] > max_temp:
                    max_temp = nums[j]
                    nums[i], nums[j] = nums[j], nums[i]
        return nums[k - 1]
        '''
        
        '''
        #method 0: naive. Sort first then return. O(NlogN), not good enough.
        nums.sort()
        return nums[-k]
        '''
