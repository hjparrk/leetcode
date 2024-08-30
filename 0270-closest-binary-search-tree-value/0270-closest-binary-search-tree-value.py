# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:

        ans = root.val
        while root:
            if abs(root.val - target) < abs(ans - target):
                ans = root.val
            
            elif abs(root.val - target) == abs(ans - target):
                ans = min(ans, root.val)
            
            if root.val > target:
                root = root.left
            else:
                root = root.right
        
        return ans

            



    