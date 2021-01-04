class Solution {

    // 2D dp where m and n are column and width 
    // if left and top edge # of ways is 1, else take sum of getting to left and top
    // O(n x m) time
    // O(n x m) space
    public int uniquePaths(int m, int n) {
        int[][] dp = new int[m][n];
        for(int i =0; i<m; i++){
            for(int j=0; j<n; j++){
                if(i==0 || j==0){
                    dp[i][j] = 1;
                }
                else{
                    dp[i][j] = dp[i-1][j] + dp[i][j-1];
                }
            }
        }
        return dp[m-1][n-1];
        // return factorial(m + n - 2) / math.factorial(n - 1);
    }
}
