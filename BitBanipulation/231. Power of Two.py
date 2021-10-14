'''
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1
'''

class Solution:
    
    #method 2. Turn off the rightmost 1 bit. O(1), S(1)
    def isPowerOfTwo(self, n: int) -> bool:    
        if n == 0: return False
        return (n & (n - 1)) == 0
    
    '''
    #method 1. get the rightmost bit. O(1), S(1)
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0: return False
        return (n & -n) == n
    '''
