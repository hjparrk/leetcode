"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        seen = {}
        def dfs(node):
            copied = Node(node.val)
            seen[copied.val] = copied

            for neighbor in node.neighbors:
                if neighbor.val in seen:
                    copied.neighbors.append(seen[neighbor.val])
                else:
                    copied.neighbors.append(dfs(neighbor))
            return copied
        return dfs(node)