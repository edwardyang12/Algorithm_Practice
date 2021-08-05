# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    # fast and slow runners
    def hasCycle(self, head: ListNode) -> bool:
        if(head==None or head.next==None or head.next.next==None):
            return False
        fast = head.next.next 
        slow = head
        
        while(fast!=None):
            if(fast==slow):
                return True
            else:
                if(fast.next!=None):
                    fast = fast.next.next 
                else:
                    fast = None
                slow = slow.next
            
        return False
        
