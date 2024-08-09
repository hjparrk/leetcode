# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        ans = []

        if not root:
            return ans

        queue = deque([root])

        while queue:

            num_nodes = len(queue)

            for i in range(num_nodes):

                node = queue.popleft()

                if i + 1 == num_nodes:
                    ans.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
        return ans

        