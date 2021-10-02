/*
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.
*/

class Solution {
    
    // DP. O(mn), S(mn)
    // Build DP matrix. DP[i][j] = text1[0:i+1], text2[0:j+1]
    public int longestCommonSubsequence(String text1, String text2) {
        int m = text1.length(), n = text2.length();
        int[][] DP = new int[m][n];
        if (text1.charAt(0) == text2.charAt(0)) DP[0][0] = 1;
        
        // calculate the values when i == 0 and j == 0;
        for (int i = 1; i < m; i++) {
            if (DP[i - 1][0] == 1) DP[i][0] = 1;
            else if (text1.charAt(i) == text2.charAt(0)) DP[i][0] = 1;
        }
        for (int j = 1; j < n; j++) {
            if (DP[0][j - 1] == 1) DP[0][j] = 1;
            else if (text1.charAt(0) == text2.charAt(j)) DP[0][j] = 1;
        }
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (text1.charAt(i) == text2.charAt(j)) DP[i][j] = 1 + DP[i - 1][j - 1];
                else DP[i][j] = Math.max(DP[i - 1][j], DP[i][j - 1]);
            }
        }
        return DP[m - 1][n - 1];
    }
}
    
    
    
    // Using Naive recursion. -> Too slow!
    // Potential Edge case error which are not validated.
    /*
    public int longestCommonSubsequence(String text1, String text2) {
        return countSubsequence(text1, text2, text1.length() - 1, text2.length() - 1);
    }
    
    private int countSubsequence(String text1, String text2, int i1, int i2) {
        if (i1 < 0 || i2 < 0) return 0;
        if (text1.charAt(i1) == text2.charAt(i2)) {
            return (1 + countSubsequence(text1, text2, i1 - 1, i2 - 1));
        } else {
            return (Math.max(countSubsequence(text1, text2, i1 - 1, i2), 
                            countSubsequence(text1, text2, i1, i2 - 1)));
        }
    }
}
    */
