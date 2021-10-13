'''
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
'''

class Solution:
    
    #method 2. Using 2 pointers. O(mn), S(1)
    def multiply(self, num1: str, num2: str) -> str:
        if (len(num1) == 1 and int(num1)== 0) or (len(num2) == 1 and int(num2)== 0): return '0'
        res = [0 for _ in range(len(num1) + len(num2))]
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                n1, n2 = int(num1[i]), int(num2[j])
                curr = n1 * n2 + res[i + j + 1]
                digit1 = curr // 10
                digit2 = curr % 10
                res[i + j] += digit1
                res[i + j + 1] = digit2
        for i in range(len(res)):
            res[i] = str(res[i])
        if res[0] == '0': return ''.join(res[1:])
        return ''.join(res)
    
    '''
    #Method 1. Life is short! Using Build-in APIs!
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1) * int(num2))
    '''
