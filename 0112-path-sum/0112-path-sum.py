# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node, curr):

            # base cases
            # root
            if not node:
                return False
            
            # leaf
            if node.left is None and node.right is None:
                return (curr + node.val) == targetSum
            
            # recursive cases
            curr += node.val
            left = dfs(node.left, curr)
            right = dfs(node.right, curr)

            return left or right
        
        return dfs(root, 0)



        

        