# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        ans = 0
        while queue:
            curr_sum = 0
            num_nodes = len(queue)

            for _ in range(num_nodes):

                node = queue.popleft()
                curr_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if not queue:
                ans = curr_sum
        
        return ans