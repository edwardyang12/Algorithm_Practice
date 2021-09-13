class Solution:
    
    def occurrences(self, word):
        occur = [0]*26
        for s in word:
            val = ord(s)-ord('a')
            occur[val]+=1
        return tuple(occur)
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # dictionary: {(tuple of occurrences of chars):(list of words)}
        anagram={}
        out = []
        for item in strs:
            temp = self.occurrences(item)
            if temp in anagram:
                anagram[temp].append(item)
            else:
                anagram[temp] = [item]
        
        for key in anagram:
            out.append(anagram[key])
        return out
