'''
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].
'''

#Using 2 Stack. O(n), S(n). n is the length of the decoded string.
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_str = []
        nums = []
        for string in s:
            if string == ']':
                curr = stack.pop()
                while curr != '[':
                    curr_str.append(curr)
                    curr = stack.pop()
                num = stack[-1]
                while ord(num) >= 48 and ord(num) <= 57:
                    nums.append(num)
                    stack.pop()
                    if stack: num = stack[-1]
                    else: break
                k = int(''.join(nums[::-1]))
                nums = []
                curr_str *= k
                while curr_str:
                    stack.append(curr_str.pop())
            else:
                stack.append(string)
        return ''.join(stack)
