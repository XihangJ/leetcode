'''
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).
'''

class Solution:
    # backtracking. O(2**N * N), S(N)
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        def backtrack(node, path):
            if path[-1] == len(graph) - 1: return
            for neighbor in graph[node]:
                if neighbor not in visited:
                    path.append(neighbor)
                    visited.add(neighbor)
                    if neighbor == len(graph) - 1: 
                        res.append(path.copy())
                    backtrack(neighbor, path)
                    path.pop()
                    visited.remove(neighbor)
        
        res = []
        visited = set()
        backtrack(0, [0])
        return res
