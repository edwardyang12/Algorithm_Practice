class Solution:

    # stack storing all positions to flood fill (DFS)
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        stack = [[sr,sc]]
        r = len(image)
        c = len(image[0])
        same = image[sr][sc]
        if same==newColor:
            return image
        while (stack):
            temp = stack.pop(0)
            image[temp[0]][temp[1]] = newColor
            if temp[0]+1 < r and image[temp[0]+1][temp[1]]==same:
                stack.append([temp[0]+1, temp[1]])
            if temp[0]-1 >= 0 and image[temp[0]-1][temp[1]]==same:
                stack.append([temp[0]-1, temp[1]])
            if temp[1]+1 < c and image[temp[0]][temp[1]+1]==same:
                stack.append([temp[0], temp[1]+1])
            if temp[1]-1 >= 0 and image[temp[0]][temp[1]-1]==same:
                stack.append([temp[0], temp[1]-1])
        return image
