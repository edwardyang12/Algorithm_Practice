# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.index = 0
 
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
 
        # at 3 
        # {9:0, 3:1, 15:2, 20:3, 7:4}
        # partition inorder into [9], [15,20,7]
        # preorder through preorder array to generate tree
 
        self.hashmap = {}
        self.preorder = preorder
        for i in range(len(inorder)):
            self.hashmap[inorder[i]] = i
 
        val = preorder[self.index]
        root = TreeNode(val)
        self.index+=1
        root.left = self.recurse(0,self.hashmap[val]-1)
        root.right = self.recurse(self.hashmap[val]+1, len(inorder)-1)
        return root
 
    # create root and then preorder traversal through left and right subtrees
    def recurse(self,left,right):
        if left>right:
            return None
 
        val = self.preorder[self.index]
        root = TreeNode(val)
        self.index+=1
        root.left = self.recurse(left,self.hashmap[val]-1)
        root.right = self.recurse(self.hashmap[val]+1, right)
        return root
