/*
Given a string s containing an out-of-order English representation of digits 0-9, return the digits in ascending order.
*/

class Solution {
    // method 1. Using hashmap. O(n), S(1)
    public String originalDigits(String s) {
        // numbers: zero, one, two, three, four, five, six, seven, eight, nine
        int[] bucket = new int[10];
        
        Map<String, Integer> count = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            String curr = String.valueOf(s.charAt(i));
            if (count.containsKey(curr)) {
                count.replace(curr, count.get(curr) + 1);
            } else {
                count.put(curr, 1);
            }
        }
        
        String[] check_list = {"zero", "six", "four", "eight", "two", "five", "seven", "one", "nine", "three"};
        String[] reference_list = {"z", "x", "u", "g", "w", "f", "v", "o", "i", "t"};
        int[] index_tofill = {0, 6, 4, 8, 2, 5, 7, 1, 9, 3};
        
        for (int i = 0; i < check_list.length; i++) {
            
            String check_s = check_list[i];
            String reference = reference_list[i];
            
            if (count.containsKey(reference)) {
                
                int reference_num = count.get(reference);
                if (reference_num <= 0) continue;
                
                bucket[index_tofill[i]] = reference_num;
                for (int j = 0; j < check_s.length(); j++) {
                    String ch_curr = String.valueOf(check_s.charAt(j));
                    count.replace(ch_curr, count.get(ch_curr) - reference_num);    
                }
            }
        }
        StringBuilder output = new StringBuilder();
        for (int i = 0; i < bucket.length; i++) {
            if (bucket[i] > 0) {
                for (int j = 0; j < bucket[i]; j++) {
                    output.append(i);
                }
            }
        }
        return output.toString();
    }
}
