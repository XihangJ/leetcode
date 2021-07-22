'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
'''

class Solution:
    
    #method 2. single for loop. O(min(m, n)), S(1)
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1 and not nums2: return
        
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m = len(nums1)
        n = len(nums2)
        if m == 0:
            if n % 2 == 0:
                return (nums2[(n - 1) // 2] + nums2[n // 2]) / 2
            else:
                return float(nums2[n // 2])
        
        leftSize = (m + n) // 2
        for i in range(m + 1):
            j = m - i
            
            if i == 0:
                leftMax = nums2[leftSize - 1]
            elif leftSize == m and i == m:
                leftMax = nums1[i - 1]
            else:
                leftMax = max(nums1[i - 1], nums2[leftSize - i - 1])
            
            if j == 0:
                rightMin = nums2[leftSize - i]
            elif n == m and j == m:
                rightMin = nums1[0]
            else:
                rightMin = min(nums1[i], nums2[leftSize - i])
            
            if leftMax <= rightMin:
                if (m + n) % 2 == 0: return (leftMax + rightMin) / 2
                else: return float(rightMin) 
    
    
    '''
    #method 1. binary search. O(log(min(m, n)))), S(1)
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1 and not nums2: return
        
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m = len(nums1)
        n = len(nums2)
        if m == 0:
            if n % 2 == 0:
                return (nums2[(n - 1) // 2] + nums2[n // 2]) / 2
            else:
                return float(nums2[n // 2])
            
        start, end = 0, m
        leftSize = (m + n) // 2
        while start + 1 < end:
            i = (start + end) // 2
            j = m - i
            
            if i == 0:
                leftMax = nums2[leftSize - 1]
            elif leftSize == m and i == m:
                leftMax = nums1[i - 1]
            else:
                leftMax = max(nums1[i - 1], nums2[leftSize - i - 1])
                    
            
            if j == 0:
                rightMin = nums2[leftSize - i]
            elif n == m and j == m:
                rightMin = nums1[0]
            else:
                rightMin = min(nums1[i], nums2[leftSize - i])
                
            if leftMax <= rightMin:
                if (m + n) % 2 == 0: return (leftMax + rightMin) / 2
                else: return float(rightMin)
            else:
                if i == 0: start = i
                elif j == 0: end = i
                elif nums1[i - 1] > nums2[leftSize - i]: end = i
                elif nums2[leftSize - i - 1] > nums1[i]: start = i
        
        for i in [start, end]:
            j = m - i

            if i == 0:
                leftMax = nums2[leftSize - 1]
            elif leftSize == m and i == m:
                leftMax = nums1[i - 1]
            else:
                leftMax = max(nums1[i - 1], nums2[leftSize - i - 1])


            if j == 0:
                rightMin = nums2[leftSize - i]
            elif n == m and j == m:
                rightMin = nums1[0]
            else:
                rightMin = min(nums1[i], nums2[leftSize - i])
                
            if leftMax <= rightMin:
                if (m + n) % 2 == 0: return (leftMax + rightMin) / 2
                else: return float(rightMin)
    '''
