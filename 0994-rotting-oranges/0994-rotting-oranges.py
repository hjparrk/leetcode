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
        
        seen = {}
        def bfs(root):
            queue = deque([(root, 0)]) # node, steps
            while queue:
                node, steps = queue.popleft()
                for neighbor in neighbors(node):
                    if neighbor not in seen:
                        seen[neighbor] = steps + 1
                        queue.append((neighbor, steps + 1))
                    else:
                        if steps + 1 < seen[neighbor]:
                            seen[neighbor] = steps + 1
                            queue.append((neighbor, steps + 1))
        
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 2:
                    bfs((row, col))
        
        ans = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    if (row, col) in seen:
                        ans = max(ans, seen[(row, col)])
                    else:
                        return -1
        return ans


