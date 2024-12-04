from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        def dfs(root):
            stack = [root]
            while stack:
                node = stack.pop()
                for neighbor in graph[node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        stack.append(neighbor)
        
        ans = 0
        seen = set()
        for node in range(n):
            if node not in seen:
                seen.add(node)
                dfs(node)
                ans += 1
        return ans

        