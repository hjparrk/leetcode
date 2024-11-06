from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n and grid[row][col] == 1

        directions = [(1,0), (-1,0), (0,-1), (0,1)]
        def neighbors(node):
            nodes = []
            row, col = node
            for dx, dy in directions:
                new_row, new_col = row + dy, col + dx
                if valid(new_row, new_col):
                    nodes.append((new_row, new_col))
            return nodes
        
        fresh, queue = 0, deque([])
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    queue.append((row, col))
        if fresh == 0:
            return 0

        steps = -1
        seen = set()
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                for neighbor in neighbors(node):
                    if neighbor not in seen:
                        seen.add(neighbor)
                        queue.append(neighbor)
            steps += 1
        return steps if len(seen) == fresh else -1

