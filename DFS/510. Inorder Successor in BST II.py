'''
Given a node in a binary search tree, return the in-order successor of that node in the BST. If that node has no in-order successor, return null.

The successor of a node is the node with the smallest key greater than node.val.

You will have direct access to the node but not to the root of the tree. Each node will have a reference to its parent node. Below is the definition for Node:
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        if node.right:
            curr = node.right
            while curr.left:
                curr = curr.left
            return curr
        elif node.parent:
            if node.parent.left == node:
                return node.parent
            else:
                curr = node.parent
                while curr.parent:
                    if curr.parent.left == curr: return curr.parent
                    else: curr = curr.parent
        return
