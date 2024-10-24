from collections import defaultdict

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n

        m, n = len(grid), len(grid[0])
        seen = {(0,0, k)}
        queue = deque([(0,0,k,0)]) # (row, col, remain, steps)
        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        while queue:
            row, col, remain, steps = queue.popleft()
            if row == m - 1 and col == n - 1:
                return steps

            for dx, dy in directions:
                new_row, new_col = row + dy, col + dx
                if valid(new_row, new_col):
                    if grid[new_row][new_col] == 0: # empty cell
                        if (new_row, new_col, remain) not in seen:
                            seen.add((new_row, new_col, remain))
                            queue.append((new_row, new_col, remain, steps + 1))
                    elif remain and (new_row, new_col, remain - 1) not in seen:
                        seen.add((new_row, new_col, remain - 1))
                        queue.append((new_row, new_col, remain - 1, steps + 1))
        return -1
        