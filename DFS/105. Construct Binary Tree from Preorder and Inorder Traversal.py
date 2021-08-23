'''
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        d = {}
        for i, node in enumerate(inorder):
            d[node] = i
        preorder_index = 0
        def convertTree(left, right):
            nonlocal preorder_index
            if left > right: return
            root_val = preorder[preorder_index]
            root = TreeNode(root_val)
            preorder_index += 1
            
            root.left = convertTree(left, d[root_val] - 1)
            root.right = convertTree(d[root_val] + 1, right)
            return root
        return convertTree(0, len(inorder) - 1)
    
