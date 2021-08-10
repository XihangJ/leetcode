'''
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
"""
#method 1. DFS. O(V + E). S(V)
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        return self.helper(node, {})
    
    def helper(self, node, visited):
        if not node: return node      
        if node in visited: 
            return visited[node]
        new_node = Node(node.val, [])
        visited[node] = new_node
        if node.neighbors:
            for curr in node.neighbors:
                new_node.neighbors.append(self.helper(curr, visited))
        return new_node
"""   
#method 2. BFS.  O(V + E). S(V)
from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return
        visited = {}
        queue = deque([node])
        visited[node] = Node(node.val, [])
        while queue:
            curr = queue.popleft()
            for neighbor in curr.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)
                visited[curr].neighbors.append(visited[neighbor])
        return visited[node]
