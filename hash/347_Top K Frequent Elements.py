'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
'''

class Solution:
    
    #method 3. Using frequency array. O(n), S(n).
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        freq = [[] for i in range(len(nums) + 1)]
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        for key in d:
            freq[d[key]].append(key)
        count = 0
        i = -1
        res = []
        while count < k:
            if freq[i]:
                for key in freq[i]:
                    if count < k:
                        res.append(key)
                        count += 1
                    else:
                        break
            i -= 1
        return res 
    '''
    #method 2. hashmap + heap. O(dlogk), S(d)
    import heapq
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}    
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        pairs = []
        for key in d:
            pairs.append([d[key], key])
        largest = heapq.nlargest(k, pairs)
        res = []
        for pair in largest:
            res.append(pair[1])
        return res
    '''
    
    '''
    #method 1. hashmap. O(dlogd), S(d). d: distinc number in nums
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        pairs = []
        for key in d:
