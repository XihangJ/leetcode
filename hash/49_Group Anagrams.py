'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''

class Solution:
    
    #method 2. Counting sort. O(nk), S(nk)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            count = [0 for _ in range(26)]
            for letter in s:
                count[ord(letter) - ord('a')] += 1
            count_tuple = tuple(count)
            if count_tuple in d:
                d[count_tuple].append(s)
            else:
                d[count_tuple] = [s]
        
        res = []
        for key in d:
            res.append(d[key])
        return res    
    
    '''
    #method 1. sorting. O(n * klogk), S(nk)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            curr_list = [letter for letter in s]
            curr_list.sort()
            curr_str = ''.join(curr_list)
            if curr_str in d:
                d[curr_str].append(s)
            else:
                d[curr_str] = [s]
        res = []
        for key in d:
            res.append(d[key])
        return res
        '''
