class Solution:

    # expanded each potential palindrome from center letter/ letters
    # found max of all palindromes
    def longestPalindrome(self, s: str) -> str:
        startL, startR = 0,0
        longest = 0
        for i in range(len(s)):
            temp = self.expand(s,i,i)
            if(temp>longest):
                startL=i
                startR=i
                longest= temp
            temp = self.expand(s,i,i+1)
            if(temp>longest):
                startL=i
                startR=i+1
                longest=temp
        if(startL!=startR):
            return s[startL-longest//2+1: startR+longest//2]
        else:
            return s[startL-longest//2: startR+longest//2+1]
            
    def expand(self, s, startL, startR):
        size = 0
        if(startL==startR):
            size = 1
            
        else:
            if(startR<len(s) and s[startL]==s[startR]):
                size = 2
            else:
                return 0
        startL-=1
        startR+=1
        while(startL>=0 and startR <len(s)):
            if(s[startL]==s[startR]):
                startL-=1
                startR+=1
                size+=2
            else:
                break
        return size
