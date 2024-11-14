from collections import defaultdict, deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]

        graph, degrees = defaultdict(list), defaultdict(int)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
            degrees[x] += 1
            degrees[y] += 1
        
        leaves = deque([node for node, degree in degrees.items() if degree == 1])
        while n > 2:
            for i in range(len(leaves)):
                node = leaves.popleft()
                n -= 1
                for neighbor in graph[node]:
                    degrees[neighbor] -= 1
                    if degrees[neighbor] == 1:
                        leaves.append(neighbor)
        return list(leaves)