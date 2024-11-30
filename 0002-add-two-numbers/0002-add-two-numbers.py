# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def calc_sum(head):
            num = 0
            curr, place = head, 1
            while curr:
                num = num + (curr.val * place)
                place *= 10
                curr = curr.next
            return num

        total = calc_sum(l1) + calc_sum(l2)
        dummy = ListNode()
        prev = dummy
        while total:
            digit = total % 10
            total = total // 10
            node = ListNode(digit)
            prev.next = node
            prev = prev.next
        return dummy.next if dummy.next else ListNode(0)
