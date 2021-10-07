/*
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
*/
class Solution {
    // method 1. 2 pointers. O(n), S(n)
    public int[] sortedSquares(int[] nums) {
        List<Integer> negative = new ArrayList<>();
        List<Integer> positive = new ArrayList<>();
        int[] results = new int[nums.length];
        // build negative and positive ArrayLists.
        for (int num : nums) {
            if (num < 0) negative.add(num * num);
            else positive.add(num * num);
        }
        // edge cases
        if (negative.size() == 0) {
            for (int i = 0; i < positive.size(); i++) results[i] = positive.get(i);
        } else if (positive.size() == 0){
            for (int i = 0; i < negative.size(); i++) results[i] = negative.get(i);
        }
        
        // build result array
        int i_res = 0;
        int i_neg = negative.size() - 1;
        int i_pos = 0;
        while (i_neg >= 0 && i_pos < positive.size()) {
            if (negative.get(i_neg) <= positive.get(i_pos)) {
                results[i_res] = negative.get(i_neg);
                i_neg--;
            } else {
                results[i_res] = positive.get(i_pos);
                i_pos++;
            }
            i_res++;
        }
        // fill the results array with remaining data.
        while (i_neg >= 0) {
            results[i_res] = negative.get(i_neg);
            i_res++;
            i_neg--;
        }
        while (i_pos < positive.size()) {
            results[i_res] = positive.get(i_pos);
            i_res++;
            i_pos++;
        }
        return results;    
    }
}
