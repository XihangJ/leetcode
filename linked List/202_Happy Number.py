'''
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
'''

class Solution:
    '''
    #method 2. Floyd's cycle-finding. O(logn), S(1)
    def isHappy(self, n: int) -> bool:
        if n == 1: return True
        slow = n
        fast = self.getNext(n)
        while slow != fast:
            if fast == 1:
                return True
            elif slow == fast:
                return False
            else:
                slow = self.getNext(slow)
                fast = self.getNext(self.getNext(fast))
    
    
    def getNext(self, n):
        if n == 1: return 1
        num = 0
        while n > 0:
            digit = n % 10
            n = n // 10
            num += digit ** 2
        return num
    '''    
        
        
    
    #method 1. detect cycles with hashset. O(logn), S(logn)
    def isHappy(self, n: int) -> bool:
        if n == 1: return True
        visited = set()
        num = 0
        while num != 1 and num not in visited:
            while n > 0:
                digit = n % 10
                n = n // 10
                num += digit ** 2
            if num == 1: 
                return True
            elif num in visited: 
                return False
            else:
                visited.add(num)
                n = num
                num = 0
