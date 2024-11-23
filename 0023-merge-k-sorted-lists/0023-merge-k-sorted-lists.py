# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        for linked_list in lists:
            curr = linked_list
            while curr:
                nodes.append(curr)
                curr = curr.next
        nodes.sort(key = lambda node: node.val)
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        if not nodes: return
        nodes[-1].next = None
        return nodes[0]
