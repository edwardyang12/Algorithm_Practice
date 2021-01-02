class Solution {

    // HashMap to store strings that have already been compared to speed up runtime
    // if start==end: dp on substring with start+1, end-1
    // else: max on either dp on substring start+1, end or start, end -1
    // O(2^n) time
    // O(2^n) space
    // could be sped up to O(n^2) with diagonal DP by forward looping through String with another backward loop inside
    // and checking if characters match, if match: 1+diagonal value, else: max of prior forward or backward
    public int longestPalindromeSubseq(String s) {
       HashMap<String, Integer> solved = new HashMap<String, Integer>();

        return dp(s, 0, s.length()-1, solved);
    }

    public int dp(String s, int start, int end, HashMap<String, Integer> solved){
        if (start>end){
            return 0;
        }
        if (start==end){
            return 1;
        }
        String small = s.substring(start,end+1);

        if(solved.containsKey(small)){
            return solved.get(small);
        }
        if(s.charAt(start)==s.charAt(end)){
            int temp = 2 + dp(s, start+1, end-1, solved);
            solved.put(small, temp);
            return temp;
        }
        else{
            int temp= Math.max(dp(s,start+1,end,solved),dp(s,start,end-1,solved));
            solved.put(small, temp);
            return temp;
        }
    }

}
