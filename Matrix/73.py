class Solution:

    # first for loop goes through each row and sets all elements in row to 0 if there is a 0
    # and sets the 0s to 0.5 (marker)
    # second for loop goes through each column 
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        x = len(matrix)
        y = len(matrix[0])
        for row in range(x):
            zero = False
            for col in range(y):
                if matrix[row][col]==0:
                    zero = True
                    break
            if zero:
                for col in range(y):
                    if matrix[row][col]==0:
                        matrix[row][col] = 0.5
                    else:
                        matrix[row][col] = 0
        for col in range(y):
            zero = False
            for row in range(x):
                if matrix[row][col]==0.5:
                    zero = True
                    break
            if zero:
                for row in range(x):
                    matrix[row][col]=0
        return matrix

                        
