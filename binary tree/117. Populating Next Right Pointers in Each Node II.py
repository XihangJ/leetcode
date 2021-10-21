'''
Given a binary tree

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
    def connect(self, root: 'Node') -> 'Node':
        if not root: return 
        if root.left:
            if root.right:
                root.left.next = root.right
            elif root.next:
                node = root.next
                while node:
                    if node.left: 
                        root.left.next = node.left
                        break
                    elif node.right: 
                        root.left.next = node.right
                        break
                    node = node.next
        if root.right:
            if root.next:
                node = root.next
                while node:
                    if node.left: 
                        root.right.next = node.left
                        break
                    elif node.right: 
                        root.right.next = node.right
                        break
                    node = node.next
        self.connect(root.right) #very important!!!!! connect root.right first!!!
        self.connect(root.left)
        return root
