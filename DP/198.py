class Solution:
    def rob(self, nums: List[int]) -> int:

        # take (i-2)+curr or not take (i-1)
        dp = [0]*(len(nums))

        for i in range(len(nums)):
            if(i==0):
                dp[i]= nums[i]
            elif(i==1):
                dp[i] = max(dp[i-1], nums[i])
            else:
                dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        return dp[len(nums)-1]
