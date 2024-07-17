# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        arr_set = set(nums)

        head_copy = ListNode()
        if head.val in arr_set:
            while  head.val in arr_set:
                head_copy.next = head.next
                head.next = None
                head = head_copy.next
        else:
            head_copy.next = head

        while head is not None and head.next is not None:
            while head.next is not None and head.next.val in arr_set:
                new_next = head.next.next
                head.next.next = None
                head.next = new_next

            head = head.next

        
        return head_copy.next