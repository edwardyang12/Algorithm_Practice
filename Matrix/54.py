class Solution:

    # computes matrix layer by layer, going clockwise
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        top = m-1
        left = 0
        right = n-1
        bot = 0
        
        i = 0
        res = [0]*(m*n)
        posx = 0
        posy = 0
        
        bot+=1
        while(i<m*n):

            
            # go right
            while(posx<=right):
                res[i] = matrix[posy][posx]
                i+=1
                posx+=1
            right-=1
            posx -=1
            posy+=1
            if(i==m*n):
                break
                
            # go down
            while(posy<=top):
                res[i] = matrix[posy][posx]
                i+=1
                posy+=1
            posy-=1
            top-=1
            posx-=1
                        
            # go left
            while(posx>=left):
                res[i] = matrix[posy][posx]
                i+=1
                posx-=1
            posx+=1
            left+=1
            posy-=1
            if(i==m*n):
                break
            
            # go up
            while(posy>=bot):
                res[i] = matrix[posy][posx]
                i+=1
                posy-=1
            posy+=1
            bot +=1
            posx+=1

            
        return res
            
