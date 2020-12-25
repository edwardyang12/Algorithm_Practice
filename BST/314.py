class Solution:

    # BFS through tree using queue
    # hashmap to store node: value
    # hashmap of value: [nodes] to store nodes at each value in top down order
    # for each node left: value - 1, right: value + 1
    # store largest and smallest values to iterate through outputmap
    # O(n) time
    # O(n) memory
    
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if root==None:
            return []
        queue = [root]
        hashmap = {root:0}
        outputmap = {0:[root.val]}
        small = 0
        large = 0
        while(len(queue)!=0):
            temp = queue.pop(0)
            order = hashmap[temp]
            if(temp!=None):
                if(temp.left):
                    queue.append(temp.left)
                    hashmap[temp.left] = order-1
                    if order-1 not in outputmap:
                        outputmap[order-1] = [temp.left.val]
                    else:
                        outputmap[order-1].append(temp.left.val)
                    if order-1<small:
                        small = order-1
                if(temp.right):
                    queue.append(temp.right)
                    hashmap[temp.right] = order+1
                    if order+1 not in outputmap:
                        outputmap[order+1] = [temp.right.val]
                    else:
                        outputmap[order+1].append(temp.right.val)
                    if order+1>large:
                        large = order+1
        
        output = []
        while(small<=large):
            output.append(outputmap[small])
            small+=1
    
        return output
