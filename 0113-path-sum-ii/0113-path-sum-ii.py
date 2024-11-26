# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        def backtrack(path, node, curr):
            if not node: return

            path.append(node.val)
            curr += node.val
            if not node.left and \
               not node.right and \
               curr == targetSum:
               ans.append(path[:])
            
            backtrack(path, node.left, curr)
            backtrack(path, node.right, curr)

            path.pop()
            return

        ans = []
        backtrack([], root, 0) # path, node, curr_sum
        return ans