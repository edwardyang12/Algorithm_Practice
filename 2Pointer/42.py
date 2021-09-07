class Solution:

    # find all "ponds" going leftward
    # then find all "ponds" going rightward
    def trap(self, height: List[int]) -> int:
        slow =0
        fast = 1
        inside = 0 
        total = 0
        if(len(height)==1):
            return 0
        while(slow<len(height) and fast<len(height)):
            if(height[slow]>height[fast]):
                inside+=height[fast]
                fast+=1
                
            else:
                total += height[slow]*(fast-slow-1)-inside
                inside = 0
                slow=fast
                fast+=1
                
        height = height[slow:]
        height.reverse()
        total += self.trap(height)
        return total
        
