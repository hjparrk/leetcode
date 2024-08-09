# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:

        ans = []
        if not root:
            return ans

        queue = deque([root])
        while queue:

            num_nodes = len(queue)
            cur_max = float("-inf")

            for _ in range(num_nodes):

                node = queue.popleft()
                cur_max = max(cur_max, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            ans.append(cur_max)
        
        return ans


        