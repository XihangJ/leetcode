'''
A binary tree is given such that each node contains an additional random pointer which could point to any node in the tree or null.

Return a deep copy of the tree.

The tree is represented in the same input/output way as normal binary trees where each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (in the input) where the random pointer points to, or null if it does not point to any node.
You will be given the tree in class Node and you should return the cloned tree in class NodeCopy. NodeCopy class is just a clone of Node class with the same attributes and constructors.
'''

# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    
    def __init__(self):
        self.d = {}
        
    def copyRandomBinaryTree(self, root: 'Node') -> 'NodeCopy':
        new_root = self.copyTree(root)
        self.assignRandom(root, new_root)
        return new_root
    
    def copyTree(self, root):
        if not root: 
            return
        new_root = NodeCopy(root.val)
        self.d[root] = new_root
        new_root.left = self.copyTree(root.left)
        new_root.right = self.copyTree(root.right)
        return new_root
    
    def assignRandom(self, root, new_root):
        if not root: return
        if root.random: new_root.random = self.d[root.random]
        self.assignRandom(root.left, new_root.left)
        self.assignRandom(root.right, new_root.right)
        return
