'''
Share
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.convertToBST(nums, 0, len(nums) - 1)
        
    def convertToBST(self, nums, left, right):
        if left > right: return
        if left == right: return TreeNode(nums[left])
        mid = left + (right - left) // 2
        return TreeNode(nums[mid], self.convertToBST(nums, left, mid - 1), self.convertToBST(nums, mid + 1, right))
