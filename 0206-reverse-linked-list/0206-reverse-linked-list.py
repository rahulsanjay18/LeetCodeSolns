# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        temp = head
        head = head.next
        temp.next = None
        
        ans = temp
        while head:
            temp = head
            head = head.next
            temp.next = None
            temp.next = ans
            ans = temp
        
        return ans