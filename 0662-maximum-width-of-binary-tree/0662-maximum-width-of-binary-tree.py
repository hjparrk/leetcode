# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        ans = 0
        queue = deque([(root, 0)]) # node, index
        while queue:
            left = right = 0
            num = len(queue)
            for i in range(num):
                node, index = queue.popleft()
                if i == 0:
                    left = index
                if i == num - 1:
                    right = index

                if node.left:
                    queue.append((node.left, index * 2 + 1))
                if node.right:
                    queue.append((node.right, index * 2 + 2))
            ans = max(ans, right - left + 1)
        return ans
                


        