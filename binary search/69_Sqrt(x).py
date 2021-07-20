'''
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.
'''


class Solution:
    #method 1. binary search. O(log x), S(1)
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left + 1 < right:
            mid = (left + right) // 2
            if mid ** 2 > x:
                right = mid
            elif mid ** 2 < x:
                left = mid
            else:
                return mid
            
        if right ** 2 <= x:
            return right
        else:
            return left
        
