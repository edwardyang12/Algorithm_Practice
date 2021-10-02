"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:

    # use dictionary to store new nodes created and later add neighbors to it
    # can do this since values are unique
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node==None:
            return None
        mapping = {} # val: new
        stack = [node]
        while(len(stack)!=0):
            temp = stack.pop(0)
            if temp.val in mapping:
                continue
            newNode = Node(temp.val)
            mapping[temp.val] = newNode
            stack.extend(temp.neighbors) 

        stack = [node]
        visited = set()
        while(len(stack)!=0):
            temp = stack.pop(0)
            if temp.val in visited:
                continue
            visited.add(temp.val)
            curr = mapping[temp.val]
            for neigh in temp.neighbors:
                curr.neighbors.append(mapping[neigh.val])
            stack.extend(temp.neighbors)
            
        return mapping[node.val]
        
