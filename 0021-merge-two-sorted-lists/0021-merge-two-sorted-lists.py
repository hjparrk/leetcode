# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = cur = ListNode()
        while list1 and list2:
            if list1.val < list2.val: # when list1 is smaller than list2
                cur.next = list1
                list1 = list1.next
            else: # when list2 is smaller than list2, or equal
                cur.next = list2
                list2 = list2.next
            cur = cur.next
            
        cur.next = list1 or list2

        return dummy.next
        