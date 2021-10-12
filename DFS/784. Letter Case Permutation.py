'''
Given a string s, we can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. You can return the output in any order.

Example 1:

Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
'''

class Solution:
    # O(n * (2 ** n)), S(n)
    # this problem is actually a variant of subset problem
    # Ex. s = "a1b2"
    # chars_index = [0, 2]
    def letterCasePermutation(self, s: str) -> List[str]:
        # 1. generate s_list and find indices of all letters
        chars_index = []
        s_list = []
        for i in range(len(s)):
            ch = s[i]
            s_list.append(ch.lower())
            if not ch.isdigit(): chars_index.append(i)
        if len(chars_index) == 0: return [s]
        # 2. generate the subsets of chars_index and get the output string accordingly
        res = []
        def backtrack(start, curr = []):
            # get the uppercase
            for index in curr:
                s_list[index] = s_list[index].upper()
            res.append(''.join(s_list))
            # get back the lowercase
            for index in curr:
                s_list[index] = s_list[index].lower()           
            
            for i in range(start, len(chars_index)):
                curr.append(chars_index[i])
                backtrack(i + 1, curr)
                curr.pop()
        
        backtrack(0, [])
        return res
