'''
Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.

Example 1:

Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
'''

class Solution:
    
    #method 2. Counter. O(nlogn), S(n)
    def frequencySort(self, s: str) -> str:
        frequency = collections.Counter(s)
        res = []
        for ch, count in frequency.most_common():
            res.append(ch * count)
        return ''.join(res)
    
    '''
    #method 1. hashmap. O(nlogn), S(n)
    def frequencySort(self, s: str) -> str:
        frequency = {}
        for ch in s:
            if ch not in frequency:
                frequency[ch] = 1
            else:
                frequency[ch] += 1
        
        curr = []
        for ch in frequency:
            curr.append([frequency[ch], ch])
        
        curr.sort(reverse = True)
        res = []
        for key in curr:
            num, ch = key
            for i in range(num):
                res.append(ch)
        return ''.join(res)
    '''
