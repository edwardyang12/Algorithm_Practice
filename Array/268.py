class Solution:

    # expected sum of first n numbers then subtract current sum
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums) 
        formula = int(n*(n+1)/2) 
        
        for i in nums: 
            formula-=i 
            
        return formula
    
