# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode()
        tail = head
        heap = []

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
        while heap:
            list_index = heapq.heappop(heap)[1]
            tail.next = lists[list_index]
            lists[list_index] = lists[list_index].next
            if lists[list_index]:
                heapq.heappush(heap, (lists[list_index].val, list_index))
            tail = tail.next

        return head.next