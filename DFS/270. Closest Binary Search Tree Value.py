'''
Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = None
    
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        if not root: return
        diff = inf
        self.dfs(root, target, diff)
        return self.res
        
    def dfs(self, root, target, diff):
        curr_diff = abs(root.val - target)
        if curr_diff < diff:
            self.res = root.val
            diff = curr_diff
        if root.left: self.dfs(root.left, target, diff)
        if root.right: self.dfs(root.right, target, diff)
