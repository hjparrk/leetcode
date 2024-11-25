# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]
        while stack:
            x, y = stack.pop()
            if not x and not y: continue
            if (x and not y) or (y and not x): return False
            if x.val != y.val: return False

            stack.append((x.left, y.left))
            stack.append((x.right, y.right))
        return True