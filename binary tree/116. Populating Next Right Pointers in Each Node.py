'''
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    
    #method 2. DFS. O(n), S(n)
    def connect(self, root: 'Node') -> 'Node':
        self.setNext(root)
        return root
    
    def setNext(self, root):
        if not root: return 
        if root.left:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
            self.setNext(root.left)
            self.setNext(root.right)
        return
    
    '''
    #method 1. BFS. O(n), S(n)
    def connect(self, root: 'Node') -> 'Node':
        if not root: return
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if node.left:
                node.left.next = node.right
                queue.append(node.left)
                queue.append(node.right)
                if node.next:
                    node.right.next = node.next.left
        return root
    '''
