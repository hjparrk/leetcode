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
        num = calc_sum(l1) + calc_sum(l2)

        dummy = ListNode(0)
        prev = dummy
        while num:
            digit, num = num % 10, num // 10
            node = ListNode(digit)
            prev.next, prev = node, node
        return dummy.next if dummy.next else dummy
