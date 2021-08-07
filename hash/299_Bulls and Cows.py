'''
You are playing the Bulls and Cows game with your friend.

You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:

The number of "bulls", which are digits in the guess that are in the correct position.
The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.
'''

class Solution:
    #method 3. One pass Hashmap. O(n), S(n)
    def getHint(self, secret: str, guess: str) -> str:    
        d = defaultdict(int)
        x, y = 0, 0
        for i, s in enumerate(secret):
            g = guess[i]
            if s == g: x += 1
            else:
                y += int(d[s] < 0) + int(d[g] > 0)
                d[s] += 1
                d[g] -= 1
        res = str(x) + 'A' + str(y) + 'B'
        return res        
    
    
    
    '''
    #method 2. Two pass Hashmap. O(n), S(n)
    def getHint(self, secret: str, guess: str) -> str:    
        d = Counter(secret)
        x, y = 0, 0
        for i, ch in enumerate(guess):
            if ch in d:
                if ch == secret[i]:
                    x += 1
                    if d[ch] <= 0: y -= 1
                elif d[ch] > 0:
                    y += 1
                d[ch] -= 1
        res = str(x) + 'A' + str(y) + 'B'
        return res
    '''
    
    '''
    #method 1. Hashmap. O(n), S(n)
    def getHint(self, secret: str, guess: str) -> str:
        d = {}
        for i, s in enumerate(secret):
            if s in d:
                d[s].add(i)
            else:
                d[s] = set([i])
        x, y = 0, 0
        visited = set([])
        for i, s in enumerate(guess):
            if s in d:
                if i in d[s]: 
                    x += 1
                    visited.add((i, s))
                    d[s].remove(i)
                    if not d[s]: d.pop(s)
        
        for i, s in enumerate(guess):
            if s in d and (i, s) not in visited:
                y += 1
                d[s].pop()
                if not d[s]: d.pop(s)
            
        res = str(x) + 'A' + str(y) + 'B'
        return res
        '''   
