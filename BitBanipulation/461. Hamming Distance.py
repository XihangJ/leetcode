'''
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, return the Hamming distance between them.
'''

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        curr = x ^ y
        count = 0
        while curr:
            if curr & 1: count += 1
            curr >>= 1
        return count
