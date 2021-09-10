'''
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].
'''

class Solution:

    
    #2. Neighbors for words + BFS (get Layers) + Backtracking.  
    
    def __init__(self):
        self.path = []
        self.res = [] 
        self.visited = set()
    
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        
        adjList = self.getAdjList(wordList)
        neighbors = self.getNeighbors(adjList, wordList, beginWord)
        min_len, layers = self.bfs(beginWord, endWord, adjList)
        if min_len == -1: return []
        self.path = [beginWord]
        self.visited.add(beginWord)
        
        def backtracking(currWord, endWord, neighbors, min_len):
            if len(self.path) == min_len - 1 and endWord in neighbors[currWord]:
                self.path.append(endWord)
                self.res.append(self.path.copy())
                self.path.pop()
                return
            elif len(self.path) == min_len - 1:
                return
            else:
                for neighbor in neighbors[currWord]:
                    if neighbor in self.visited or neighbor not in layers[len(self.path) + 1]: continue
                    self.visited.add(neighbor)
                    self.path.append(neighbor)
                    
                    backtracking(neighbor, endWord, neighbors, min_len)
                    
                    self.visited.remove(neighbor)
                    self.path.pop()
                    
        backtracking(beginWord, endWord, neighbors, min_len)
        return self.res              
    
    def bfs(self, beginWord, endWord, adjList):
        count = 1
        min_len = inf
        layers = {1: beginWord}
        queue = collections.deque([beginWord])
        visited = set([beginWord])
        while queue:
            count += 1
            curr_len = len(queue)
            for _ in range(curr_len):
                word = queue.popleft()
                word_tmp = [ch for ch in word]
                for i in range(len(word_tmp)):
                    word_tmp_copy = word_tmp.copy()
                    word_tmp_copy[i] = '*'
                    curr_str = ''.join(word_tmp_copy)
                    if curr_str not in adjList: continue
                    for neighbor in adjList[curr_str]:
                        
                        if count not in layers: layers[count] = set([neighbor])
                        else: layers[count].add(neighbor)
                        
                        if neighbor == endWord: 
                            min_len = min(count, min_len)
                        elif neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
                            
        if min_len == inf: return -1, layers
        return min_len, layers        
        
    def getAdjList(self, wordList):
        adjList = {}
        for word in wordList:
            curr_word = []
            for ch in word:
                curr_word.append(ch)
            for i in range(len(curr_word)):
                curr_word_copy = curr_word.copy()
                curr_word_copy[i] = '*'
                curr_str = ''.join(curr_word_copy)
                if curr_str in adjList:
                    adjList[curr_str].add(word)
                else:
                    adjList[curr_str] = set([word])
        return adjList
    
    def getNeighbors(self, adjList, wordList, beginWord):
        neighbors = {}
        wordList.append(beginWord)
        for word in wordList:
            curr_word = []
            for ch in word:
                curr_word.append(ch)  
            for i in range(len(curr_word)):
                curr_word_copy = curr_word.copy()
                curr_word_copy[i] = '*'
                curr_str = ''.join(curr_word_copy)
                if curr_str in adjList:
                    for neighbor in adjList[curr_str]:
                        if word not in neighbors: neighbors[word] = set([neighbor])
                        else: neighbors[word].add(neighbor)
        return neighbors
    
    '''
    #1. adjList for 'a*b' + BFS + Backtracking. Time limit exceeded because missing dict_layers
    
    def __init__(self):
        self.path = []
        self.res = [] 
        self.visited = set()
    
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        
        adjList = self.getAdjList(wordList)
        min_len = self.bfs(beginWord, endWord, adjList)
        if min_len == -1: return []
        self.path = [beginWord]
        self.visited.add(beginWord)
        
        def backtracking(currWord, endWord, adjList, min_len):
            for ch_index in range(len(currWord)):
                word_tmp = [ch for ch in currWord]
                word_tmp[ch_index] = '*'
                curr_str = ''.join(word_tmp)
                
                if curr_str in adjList:
                    for neighbor in adjList[curr_str]:
                        
                        if neighbor not in self.visited:
                            if neighbor == endWord:
                                if len(self.path) == min_len - 1:
                                    self.path.append(neighbor)
                                    self.res.append(self.path.copy())
                                    self.path.pop()
                                return
                            if len(self.path) >= min_len: 
                                return
                                 
                            self.path.append(neighbor)
                            self.visited.add(neighbor)
                            
                            backtracking(neighbor, endWord, adjList, min_len)
                            
                            self.path.pop()
                            self.visited.remove(neighbor)
                            
        backtracking(beginWord, endWord, adjList, min_len)
        return self.res
                    
    
    def bfs(self, beginWord, endWord, adjList):
        count = 1
        queue = collections.deque([beginWord])
        visited = set([beginWord])
        while queue:
            count += 1
            curr_len = len(queue)
            for _ in range(curr_len):
                word = queue.popleft()
                word_tmp = [ch for ch in word]
                for i in range(len(word_tmp)):
                    word_tmp_copy = word_tmp.copy()
                    word_tmp_copy[i] = '*'
                    curr_str = ''.join(word_tmp_copy)
                    if curr_str not in adjList: continue
                    for neighbor in adjList[curr_str]:
                        if neighbor == endWord: 
                            return count
                        elif neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
        return -1        
        
    def getAdjList(self, wordList):
        adjList = {}
        for word in wordList:
            curr_word = []
            for ch in word:
                curr_word.append(ch)
            for i in range(len(curr_word)):
                curr_word_copy = curr_word.copy()
                curr_word_copy[i] = '*'
                curr_str = ''.join(curr_word_copy)
                if curr_str in adjList:
                    adjList[curr_str].add(word)
                else:
                    adjList[curr_str] = set([word])
        return adjList
    '''
