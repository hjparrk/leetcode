from collections import defaultdict

class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:

        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        seen = set(restricted)
        seen.add(0)
        def dfs(node):
            count = 1
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    count += dfs(neighbor)
            return count
        return dfs(0)

        