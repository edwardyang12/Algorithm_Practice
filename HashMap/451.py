class Solution:

    # hashmap to store frequency of each letter {letter: frequency}
    # hashmap to frequency: set {frequency: set{letters}}
    # max frequency
    # decrement from max while writing to array
    # array converted to string since array operations are faster
    # O(n) time
    # O(n) memory
    
    def frequencySort(self, s: str) -> str:
        
        letters = {}
        frequency = {}
        maxF = 0
        temp = 0
        newStr = []
        for char in s:
            if char in letters:
                letters[char]+=1
                temp = letters[char]
                if temp>maxF:
                    maxF = temp
                
            else:
                letters[char]=1
                temp = 1
                if maxF==0:
                    maxF=1
            
            if temp not in frequency:
                frequency[temp] = set()
                frequency[temp].add(char)
                
            else:
                frequency[temp].add(char)
                
            if temp!=1:
                    frequency[temp-1].remove(char)
        for val in range(maxF,0,-1):
            if val in frequency:
                for char in frequency[val]:
                    newStr.append(char * val)
        return "".join(newStr)
