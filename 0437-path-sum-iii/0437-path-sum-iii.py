# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        sums = defaultdict(int)
        sums[0] = 1

        def dfs(node, total):
            if not node: return 0
            total += node.val
            count = sums[total - targetSum]

            sums[total] += 1
            count += dfs(node.left, total) + dfs(node.right, total)
            sums[total] -= 1
        
            return count

        return dfs(root, 0)