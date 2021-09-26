/*
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
*/

class Solution {
    
    // Method 2. Dynamic Programming. O(n), S(1)
    public int[] countBits(int n) {
        if (n == 0) return (new int[] {0});
        int[] results = new int[n + 1];
        // the first element.
        results[0] = 0;
        // [lower_bound, upper_bound)
        int lower_bound = 1;
        int upper_bound = 2;
        int lower_pointer = 0;
        while (upper_bound <= n) {
            for (int upper_pointer = lower_bound; upper_pointer < upper_bound; upper_pointer++) {
                results[upper_pointer] = results[lower_pointer] + 1;
                lower_pointer++;
            }
            lower_bound = upper_bound;
            upper_bound <<= 1;
            lower_pointer = 0;
        }
        for (int upper_pointer = lower_bound; upper_pointer <= n; upper_pointer++) {
            results[upper_pointer] = results[lower_pointer] + 1;
            lower_pointer++;
        }
        return results;
    }
}
    
/*
    // Method 1. O(nlogn), S(1)
    public int[] countBits(int n) {
        int[] results = new int[n + 1];
        for (int i = 0; i <= n; i++) {
            results[i] = getCount(i);
        }
        return results;
    }
    
    private int getCount(int n) {
        int count = 0;
        int mask = 1;
        for (int i = 0; i < 32; i++) {
            if ((mask & n) != 0) count++;
            mask <<= 1;
        }
        return count;
    }
}
*/
