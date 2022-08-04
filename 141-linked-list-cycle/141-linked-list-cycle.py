# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        s = head
        f = head
        
        while s != None:
            
            if f.next and f.next.next:
                s = s.next
                f = f.next.next
            else:
                return False
            if s == f:
                return True
        
        return False