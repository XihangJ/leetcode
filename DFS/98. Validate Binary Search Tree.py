'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        return self.dfs(root, inf, -inf)
        
        
    def dfs(self, root, upper_bound, lower_bound):
        if root.left and (root.left.val >= root.val or root.left.val <= lower_bound): 
            return False
        if root.right and (root.right.val <= root.val or root.right.val >= upper_bound): 
            return False
        if not root.left and not root.right: 
            return True
        
        if root.left and root.right:
            return self.dfs(root.left, root.val, lower_bound) and self.dfs(root.right, upper_bound, root.val)
        elif root.left:
            return self.dfs(root.left, root.val, lower_bound)
        elif root.right:
            return self.dfs(root.right, upper_bound, root.val)
