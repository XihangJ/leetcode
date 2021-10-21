'''
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.
'''

class Solution:
    # method 1. BFS. Using adj list. O(n ** 2), S(n)
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        adjList = {}
        for row in range(n):
            adjList[row] = set()
            for col in range(n):
                if isConnected[row][col] == 1:
                    adjList[row].add(col)
        
        def bfs(row):
            queue.append(row)
            visited.add(row)
            while queue:
                curr = queue.popleft()
                for neighbor in adjList[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
        print(adjList)                
        visited = set()
        queue = collections.deque()
        count = 0
        for row in range(n):
            if row not in visited:
                count += 1
                bfs(row)
        return count
                    
