from collections import defaultdict

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        if source == destination:
            return True

        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        seen = {source}
        def dfs(node):
            for neighbor in graph[node]:
                
                if neighbor == destination:
                    return True

                if neighbor not in seen:
                    seen.add(neighbor)
                    if dfs(neighbor):
                        return True
            
            return False
            
        return dfs(source)