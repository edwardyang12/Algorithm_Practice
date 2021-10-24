class Solution:

    # tokenize and compare
    def tokenize(self,s):
        temp = [0]*26
        for i in s:
            temp[ord(i)-ord('a')]+=1
        return tuple(temp)
    def isAnagram(self, s: str, t: str) -> bool:
        return self.tokenize(s)==self.tokenize(t)
