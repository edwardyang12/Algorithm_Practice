class Solution {

    // iterate through string and check if substring(i-1,i+1)<= 26, if so dp[i] = dp[i-1] + dp[i-2]
    // if zero check previous element for what to do
    // else dp[i] = dp[i-1] because letter has be to be single number
    // O(n) time
    // O(n) space
    public int numDecodings(String s) {
        int[] dp = new int[s.length()];
        for(int i =0; i< s.length(); i++){
            if(i==0 && Integer.parseInt(s.substring(i,i+1))!=0){
                dp[0] = 1;
            }
            else if(Integer.parseInt(s.substring(i,i+1))==0){
                if(i==0){
                    return 0;
                }
                else if(i==1 && Integer.parseInt(s.substring(i-1,i+1))<=26){
                    dp[i] = 1;
                }
                else if(Integer.parseInt(s.substring(i-1,i+1))>26 || Integer.parseInt(s.substring(i-1,i+1))==0){
                    dp[i]=0;
                }
                else{
                    dp[i] = dp[i-2];
                }
            }
            else if(Integer.parseInt(s.substring(i-1,i+1))<=26 && Integer.parseInt(s.substring(i-1,i))!=0){
                if(i-2<0){
                    dp[i]= dp[i-1]+1;
                }
                else{
                    dp[i] = dp[i-1] + dp[i-2];
                }
            }
            else{
                dp[i] = dp[i-1];
            }
            System.out.println(Arrays.toString(dp));
        }
        return dp[s.length()-1];
    }

}
