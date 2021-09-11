# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        mid = head
        fast = head
        stack = []
        
        # find mid point using fast(2)/slow method
        while(fast.next!=None and fast.next.next!=None):
            fast= fast.next.next
            mid = mid.next
            
        fast = mid
        # create second list
        while(mid!=None):
            stack.append(mid)
            mid = mid.next
        
        mid = head
        temp = head
        # combine lists
        while(fast!=stack[-1]):
            temp = mid.next
            mid.next = stack.pop()
            mid.next.next = temp
            mid = temp
        
        mid.next = None
