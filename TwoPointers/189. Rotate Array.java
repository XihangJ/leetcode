/*
Given an array, rotate the array to the right by k steps, where k is non-negative.
*/

// A more straight forward method: 1)reverse entireA[]. 2) reverse A[:k+1] and A[k+1:]

class Solution {
    // method 1. Jump number. O(n), S(1)
    public void rotate(int[] nums, int k) {
        k %= nums.length;
        if (k == 0) return;
        int count = 0;
        int index_start = 0;
        while (count < nums.length) {
            int index_next = (index_start + k) % nums.length;
            int prev = nums[index_start];
            int curr;
            while (index_next != index_start) {
                curr = nums[index_next];;
                nums[index_next] = prev;
                prev = curr;
                count++;
                index_next = (index_next + k) % nums.length;
            }
            nums[index_start] = prev;
            count++;
            index_start += 1;
        }
    }
}
