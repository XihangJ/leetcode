'''
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.
'''

class Solution:
    #method 1. using stack. O(n), S(n)
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        res = []
        for a in asteroids:
            if a > 0: stack.append(a)
            else:
                while a < 0:
                    if stack: 
                        front = stack.pop()
                        if abs(a) > abs(front): continue
                        elif abs(a) == abs(front): break
                        else:
                            a = front
                            stack.append(front)
                    else:
                        res.append(a)
                        break
        res += stack
        return res
