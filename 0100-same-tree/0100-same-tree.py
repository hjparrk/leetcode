# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(x, y):
            if not x and not y:
                return True

            if not x or not y:
                return False

            if x.val != y.val:
                return False
            
            left = dfs(x.left, y.left)
            right = dfs(x.right, y.right)
            return left and right
        return dfs(p, q)
        