/*
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, 
construct and return the binary tree.
*/

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    // O(n), S(n)
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        
        // construct inorder HashMap to make finding node value faster.
        Map<Integer, Integer> map_inorder = new HashMap<>();
        for (int i = 0; i < preorder.length; i++) {
            map_inorder.put(inorder[i], i);
        }
        
        return constructTree(preorder, inorder, 0, preorder.length, 0, inorder.length, map_inorder);
    }
    
    private TreeNode constructTree(int[] preorder, int[] inorder, 
                                   int pre_start, int pre_end, int in_start, int in_end, 
                                   Map<Integer, Integer> map_inorder) {
        
        if (pre_start >= pre_end || in_start >= in_end) return null;
        
        // the first element of preorder should be the root of the output tree.
        int root_val = preorder[pre_start];
        TreeNode node = new TreeNode(root_val);
        
        // recursively generate node.left and node.right 
        // calculate the traversal range of children trees.
        int pre_start_left = pre_start + 1;
        int pre_end_left = pre_start_left + map_inorder.get(root_val) - in_start;
        int in_start_left = in_start;
        int in_end_left = map_inorder.get(root_val);        
        
        int pre_start_right = pre_end_left;
        int pre_end_right = pre_end;    
        int in_start_right = in_end_left + 1;
        int in_end_right = in_end;        
        
        node.left = constructTree(preorder, inorder, 
                                  pre_start_left, pre_end_left, in_start_left, in_end_left, 
                                  map_inorder);
        node.right = constructTree(preorder, inorder, 
                                   pre_start_right, pre_end_right, in_start_right, in_end_right, 
                                   map_inorder);
        return node;
        
    }
}
