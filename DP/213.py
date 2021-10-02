class Solution:

    # original house robber except modified on [0,n-1] and [1,n]
    # because those aren't cycles
    def rob(self, nums: List[int]) -> int:
        house1=[0]*(len(nums)-1)
        house2=[0]*(len(nums)-1)
        if(len(nums)==1):
            return nums[0]
        
        # house1
        for i in range(len(nums)-1):
            if i==0:
                house1[i] = nums[i]
                house2[i] = nums[i+1]
            elif i==1:
                house1[i] = max(nums[i], house1[i-1])
                house2[i] = max(nums[i+1], house2[i-1])
            else:
                house1[i] = max(house1[i-1],house1[i-2]+nums[i])
                house2[i] = max(house2[i-1],house2[i-2]+nums[i+1])
        return max(house1[len(nums)-2], house2[len(nums)-2])
