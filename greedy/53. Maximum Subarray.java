/*
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.
*/

class Solution {
    // Single pass. O(n), S(1)
    public int maxSubArray(int[] nums) {
        int max_sum = Integer.MIN_VALUE;
        int curr_sum = 0;
        for (int num : nums) {
            curr_sum += num;
            max_sum = Math.max(max_sum, curr_sum);
            if (curr_sum < 0) curr_sum = 0;
        }
        return max_sum;
    }
}
