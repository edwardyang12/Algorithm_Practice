class Solution:

    # row filter and then column filter to remove any rows with
    # more than one
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        valid = set() # (i,j)
        m = len(picture)
        n = len(picture[0])
        
        # row filter
        for i in range(m):
            temp = set()
            for j in range(n):
                if picture[i][j]=='B':
                    temp.add((i,j))
            if len(temp)==1:
                valid.update(temp)
        # column filter
        for j in range(n):
            temp = set()
            for i in range(m):
                if picture[i][j] == 'B':
                    temp.add((i,j))
            if len(temp)!=1:
                for pixel in temp:
                    if pixel in valid:
                        valid.remove(pixel)
        
        return len(valid)
