# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        nodes = list()
        for head in lists:
            cur = head
            while cur:
                nodes.append(cur)
                cur = cur.next
        
        nodes.sort(key = lambda node: node.val)

        for i, node in enumerate(nodes):
            if i + 1 == len(nodes):
                node.next = None
                continue
            node.next = nodes[i + 1]
        
        return nodes[0] if nodes else None