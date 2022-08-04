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
        
        tracker = set()
        
        while head != None:
            tracker.add(head)
            head = head.next
            if head in tracker:
                return True
        return False