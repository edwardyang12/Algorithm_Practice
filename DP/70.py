class Solution:

    # n is based on n-1, n-2 since u add either 1 or 2 steps
    def climbStairs(self, n: int) -> int:
        if(n==1):
            return 1
        dp = [0]*n
        dp[0] = 1
        dp[1] = 2
        for i in range(n):
            if i!=0 and i!=1:
                dp[i]= dp[i-1]+dp[i-2]
        return dp[n-1]
        
