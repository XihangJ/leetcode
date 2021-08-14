'''
ou have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.
'''

class Solution:
    #method 1. BFS. O(n), S(n)
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n == 1: return 1
        graph = self.convertGraph(edges)
        unvisited = set([i for i in range(n)])
        count = 0
        queue = collections.deque([])
        while unvisited:
            count += 1
            node = unvisited.pop()
            queue.append(node)
            while queue:
                node = queue.popleft()
                if node not in graph:
                    break
                for neighbor in graph[node]:
                    if neighbor in unvisited:
                        queue.append(neighbor)
                        unvisited.remove(neighbor)
        return count
        
    def convertGraph(self, edges):
        graph = {}
        for edge in edges:
            n1, n2 = edge
            if n1 not in graph: 
                graph[n1] = [n2]
            else: graph[n1].append(n2)
            if n2 not in graph: 
                graph[n2] = [n1]
            else: graph[n2].append(n1)
        return graph
