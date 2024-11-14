from collections import defaultdict, deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]
    

        graph = defaultdict(set)
        for x, y in edges:
            graph[x].add(y)
            graph[y].add(x)
        
        leaves = [node for node in range(n) if len(graph[node]) == 1]
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for node in leaves:
                neighbor = graph[node].pop()
                graph[neighbor].remove(node)
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves
        return leaves