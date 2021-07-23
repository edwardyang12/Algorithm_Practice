class Solution:

    # forward multiplies by all factors before
    # backward multiplies by all factors after
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        temp = [nums[0]]*len(nums)
        i=0
        mult = 1
        while(i<len(nums)-1):
            mult = mult*nums[i]
            temp[i+1]= mult
            i+=1
        mult = 1
        while(i>=1):
            mult = mult*nums[i]
            temp[i-1] = temp[i-1]*mult
            i-=1
            
        return temp
