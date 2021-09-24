'''
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #mehthod 1. DFS. O(n), S(n)
    def goodNodes(self, root: TreeNode) -> int:
        
        return self.countGoodNode(root, root.val)
        
        
    def countGoodNode(self, root, root_max):
        if not root: return 0
        if not root.left and not root.right:
            if root.val >= root_max:
                return 1
            else:
                return 0
        else:
            #root_max = max(root_max, root.val)
            if root.left and root.right:
                res = self.countGoodNode(root.left, max(root.left.val, root_max)) + self.countGoodNode(root.right, max(root.right.val, root_max))
            elif root.left:
                res = self.countGoodNode(root.left, max(root.left.val, root_max))
            else:
                res = self.countGoodNode(root.right, max(root.right.val, root_max))
            if root.val >= root_max:
                return 1 + res
            return res
                
