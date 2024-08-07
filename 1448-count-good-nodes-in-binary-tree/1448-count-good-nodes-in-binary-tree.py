# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        ans = 0
        max_val = float("-inf")
        stack = [(root, max_val)]

        while stack:

            node, max_val = stack.pop()
            if node.val >= max_val:
                ans += 1
                max_val = node.val

            if node.left:
                stack.append((node.left, max_val))
            if node.right:
                stack.append((node.right, max_val))
        
        return ans
        