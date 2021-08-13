'''
You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.
'''


class Solution:
    #method 1. Convert graph to adjacent list then BFS.
    #O(V + E), S(V)
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: return False
        if not edges: return True
        root, adjList = self.convertGraph(edges)
        visited = set([])
        queue = collections.deque([root])
        count = 0
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                count += 1
            for neighbor in adjList[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
        return count == n
                  
    def convertGraph(self, edges):
        if not edges: return 
        adjList = {}
        for edge in edges:
            node1, node2 = edge
            if node1 in adjList: adjList[node1].append(node2)
            else: adjList[node1] = [node2]
            if node2 in adjList: adjList[node2].append(node1)
            else: adjList[node2] = [node1]
        return node1, adjList
