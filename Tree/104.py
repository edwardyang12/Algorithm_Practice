# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # DFS 
    def maxDepth(self, root: TreeNode) -> int:
        temp = 0
        if(root):
            temp = 1
            if(root.left):
                temp =  max(temp, 1+ self.maxDepth(root.left))
            if(root.right):
                temp = max(temp, 1 + self.maxDepth(root.right))           
            
        return temp
