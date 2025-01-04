# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(x, y):
            if x and y:
                if x.val != y.val:
                    return False
                else:
                    return dfs(x.left, y.left) and dfs(x.right, y.right)
            elif not x and not y:
                return True
            else:
                return False
        
        stack, rootNode = [root], None
        while stack:
            node = stack.pop()
            if node.val == subRoot.val and dfs(node, subRoot):
                return True
            
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
        return False