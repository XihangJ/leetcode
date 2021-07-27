'''
You are given an array of positive integers w where w[i] describes the weight of ith index (0-indexed).

We need to call the function pickIndex() which randomly returns an integer in the range [0, w.length - 1]. pickIndex() should return the integer proportional to its weight in the w array. For example, for w = [1, 3], the probability of picking the index 0 is 1 / (1 + 3) = 0.25 (i.e 25%) while the probability of picking the index 1 is 3 / (1 + 3) = 0.75 (i.e 75%).

More formally, the probability of picking index i is w[i] / sum(w).
'''

class Solution:
    #method 1. prefix sum and binary search. O(n + logn), S(n)
    def __init__(self, w: List[int]):
        prefixSum = 0
        self.prefixSums = []
        for num in w:
            prefixSum += num
            self.prefixSums.append(prefixSum)
        self.totalSum = prefixSum

    def pickIndex(self) -> int:
        target = random.random() * self.totalSum
        left, right = 0, len(self.prefixSums) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if self.prefixSums[mid] == target: return mid
            elif self.prefixSums[mid] > target:
                right = mid
            else:
                left = mid
        if self.prefixSums[left] > target: return left
        else: return right

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
