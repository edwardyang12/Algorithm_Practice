class Node:
    def __init__(self):
        self.vals = {}
        self.end = False
    
    def insert(self,letter):
        self.vals[letter] = Node()
    
    def exist(self, letter):
        if letter in self.vals:
            return True
        else:
            return False
        
    def next(self, letter):
         return self.vals[letter]
    
class Trie:

    # connections are the characters
    # boolean to see if the letter is an end value
    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        temp = self.root
        for i in word:
            if not temp.exist(i):
                temp.insert(i)
            temp = temp.next(i)
        temp.end = True
        

    def search(self, word: str) -> bool:
        temp = self.root
        for i in word:
            if not temp.exist(i):
                return False
            temp = temp.next(i)
        if(not temp.end):
            return False
        return True
        

    def startsWith(self, prefix: str) -> bool:
        temp = self.root
        for i in prefix:
            if not temp.exist(i):
                return False
            temp = temp.next(i)
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
