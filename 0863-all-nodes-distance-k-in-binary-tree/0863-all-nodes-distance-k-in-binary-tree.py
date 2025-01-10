# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        # transform into undirected graph
        parents = dict()
        def dfs(node, parent):
            if not node:
                return None
            parents[node] = parent
            dfs(node.left, node)
            dfs(node.right, node)
        dfs(root, None)

        # start bfs from the target node
        distance = 0
        seen = {target}
        queue = deque([target])
        while queue and distance < k:
            num_nodes = len(queue)
            for _ in range(num_nodes):
                node = queue.popleft()
                for neighbor in [node.left, node.right, parents[node]]:
                    if neighbor and neighbor not in seen:
                        seen.add(neighbor)
                        queue.append(neighbor)
            distance += 1
        return [node.val for node in queue]
        