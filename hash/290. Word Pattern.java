/*
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
*/
class Solution {
    // method 1. HashMap + HashSet. O(n), O(n)
    public boolean wordPattern(String pattern, String s) {
        String[] words = s.split(" ");
        Map<Character, String> map = new HashMap<>();
        Set<String> seen = new HashSet<>();
        if (words.length != pattern.length()) return false;
        for (int i = 0; i < pattern.length(); i++) {
            char ch = pattern.charAt(i);
            String word = words[i];
            if (!map.containsKey(ch)) {
                if (seen.contains(word)) return false;
                map.put(ch, word);
                seen.add(word);
            } else {
                if (!map.get(ch).equals(word)) return false;
            }
        }
        return true;
    }
}
