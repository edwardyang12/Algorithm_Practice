class Solution {


    // use 2 pointers to check for palindromes where center is 1 or 2 char
    // increment outward from this center to determine other palindromes
    // O(n^2) time
    // O(1) space
    public int countSubstrings(String s) {
        int total = s.length();
        int start = 0;
        int end = 0;
        while(start<s.length()){
            total += pivot(s, start, end) -1;
            start++;
            if(start<s.length() && s.charAt(start)==s.charAt(end)){
                total += pivot(s,start,end);
            }
            end++;
        }
        return total;
    }
    public int pivot(String s, int start, int end){
        int total = 0;
        while(end>=0 && start< s.length() && s.charAt(start)==s.charAt(end)){
            total++;
            start++;
            end--;
        }
        return total;
    }
}
