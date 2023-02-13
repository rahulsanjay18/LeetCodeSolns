# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        h_cpy = head
        
        ct = 0
        while head:
            ct += 1
            head = head.next
            
        
        target = ct // 2
        head = h_cpy
        while target > 0:
            target -= 1
            head = head.next
        
        return head