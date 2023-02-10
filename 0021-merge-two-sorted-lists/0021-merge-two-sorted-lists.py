# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return None
        elif list1 == None:
            return list2
        elif list2 == None:
            return list1
        
        ans = None
        ans_ptr = None
        while True:
            if list1.val < list2.val:
                prev = list1
                list1 = list1.next
                prev.next = None

                if ans == None:
                    ans = prev
                    ans_ptr = prev
                else:
                    ans_ptr.next = prev
                    ans_ptr = ans_ptr.next
                if list1 == None:
                    ans_ptr.next = list2
                    break
            else:
                prev = list2
                list2 = list2.next
                prev.next = None

                if ans == None:
                    ans = prev
                    ans_ptr = prev
                else:
                    ans_ptr.next = prev
                    ans_ptr = ans_ptr.next
                
                if list2 == None:
                    ans_ptr.next = list1
                    break
        return ans