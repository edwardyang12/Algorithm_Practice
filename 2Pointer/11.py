class Solution:

    # gradually decrease left and right checking everytime height increases
    def maxArea(self, height: List[int]) -> int:
        large = 0 
        left = 0
        right = len(height)-1
 
        # ensure left side is always to the left of the right side
        while(left<right):
            h = min(height[left],height[right])
            large = max(large, (right-left)*h) # overall largest by comparing largest with current area
 
            while(left< right and height[left]<=h): # if left height greater than right height decrement right (maximize height wise)
                left+=1
            while(left<right and height[right]<=h):
                right-=1
 
        return large
