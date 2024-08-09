# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        ans = []
        if not root:
            return ans
        
        depth = 0
        queue = deque([root])
        while queue:
            sub_ans = deque()
            num_nodes = len(queue)
            for _ in range(num_nodes):
                node = queue.popleft()
                if depth % 2 == 0:
                    sub_ans.append(node.val)
                else:
                    sub_ans.appendleft(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(sub_ans)
            depth += 1
        
        return ans


