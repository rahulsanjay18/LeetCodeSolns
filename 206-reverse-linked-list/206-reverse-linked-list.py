# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        ans = None
        
        while head != None:
            popped, head = self.pop_ll(head)
            ans = self.append_to_ll(ans, popped)
        
        return ans
    
    
    def pop_ll(self, head):
        
        popped = head
        new_head = head.next
        head.next = None
        
        return popped, new_head
    
    def append_to_ll(self, ll, to_add):
        
        if ll == None:
            return to_add
        
        to_add.next = ll
        
        return to_add