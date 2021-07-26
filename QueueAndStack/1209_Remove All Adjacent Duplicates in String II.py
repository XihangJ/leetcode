'''
You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.
'''


class Solution:
    #method 1. Stack. O(nk), S(n)
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        count = 0
        for digit in s:
            if not stack:
                stack.append(digit)
                count = 1
            else:
                if digit == stack[-1]:
                    count += 1
                else:
                    count = 1
                    
                if count != k:
                    stack.append(digit)
                else:
                    for _ in range(k - 1):
                        stack.pop()
                    
                    if not stack: count = 0
                    else:
                        count = 0
                        i, curr = 1, stack[-1]
                        while i <= len(stack):
                            if stack[-i] == curr:
                                count += 1
                                i += 1
                            else:
                                break
        return ''.join(digit for digit in stack)
