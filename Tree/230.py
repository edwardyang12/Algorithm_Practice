# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        stack = []
        # go to smallest (all the way left)
        #   while adding all intermediate nodes into stack
        # go to next largest (if can go right go right and all the way down else go one up)
        #   add new list in front of old list
        # every pop operation k-1 until 1 which is the target
        
        # if list empty, go right from root and all the way left and repeat
        
        temp = root
        while(temp!=None):
            stack.append(temp)
            temp = temp.left
        while(k>1 and len(stack)!=0):
            k-=1
            temp = stack.pop()
            if(temp.right!=None):
                temps = []
                temp = temp.right
                while(temp!=None):
                    temps.append(temp)
                    temp = temp.left
                stack = stack + temps
        if(k!=1):
            stack = []
            temp = root
            while(k>1):
                if(len(stack)==0): # go right and then all the way left
                    if(temp.right!=None):
                        temps = []
                        temp = temp.right
                        while(temp!=None):
                            temps.append(temp)
                            temp = temp.left
                        stack = stack + temps
                else:
                    k-=1
                    temp = stack.pop()
        return stack.pop().val
                            
        
        
