/*
You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.
*/

import java.lang.Math;
class Solution {
    public int arrangeCoins(int n) {
        
        double depth = (-1 + Math.sqrt(8 * (long)n + 1)) / 2;
        System.out.println(Math.sqrt(1 + 8 * n));
        return (int)depth;
    }
}
