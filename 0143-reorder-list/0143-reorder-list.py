# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverse_list(self, head):
        prev, curr = None, head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find the mid node
        dummy = ListNode(0, head)
        slow = fast = dummy
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # divide the linkedlist in half
        A = dummy.next
        B = slow.next
        slow.next = None
        
        # reverse the second list
        B = self.reverse_list(B)

        # merge
        curr = ListNode()
        while A and B:
            curr.next = A
            curr = A
            A = A.next
            
            curr.next = B
            curr = B
            B = B.next
        curr.next = A