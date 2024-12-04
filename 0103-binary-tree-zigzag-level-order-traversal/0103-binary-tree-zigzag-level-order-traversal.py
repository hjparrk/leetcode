# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        ans, level = [], 0
        queue = deque([root])
        while queue:
            nodes = []

            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                nodes.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if level % 2:
                nodes.reverse()
            ans.append(nodes[:])
            level += 1

        return ans