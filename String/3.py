class Solution:

    # dictionary to store locations of all characters in substring
    # sliding window that changes start whenever repeat characters and character in substring
    def lengthOfLongestSubstring(self, s: str) -> int:
        large = 0
        start = 0
        traversed = dict()
        for i in range(len(s)):
            if s[i] not in traversed or traversed[s[i]]<start:
                traversed[s[i]] = i
            else:
                start = traversed[s[i]]+1
                traversed[s[i]] = i
            large = max(large, i-start+1)
        
        return large
