# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        h_cpy = head
        s = set()
        query = None
        while head:
            if head not in s:
                s.add(head)
                head = head.next
            else:
                query = head
                break
        if not query:
            return query
        
        head = h_cpy
        i = 0
        while head:
            if head != query:
                head = head.next
                i += 1
            else:
                return head