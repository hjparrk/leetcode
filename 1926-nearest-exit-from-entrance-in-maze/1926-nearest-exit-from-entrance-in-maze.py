from collections import defaultdict

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n and maze[row][col] == "."
        
        def is_exit(row, col):
            return (row == 0 or row == m - 1
                    or col == 0 or col == n - 1)

        m, n = len(maze), len(maze[0])
        enter_row, enter_col = entrance[0],entrance[1]
        seen = {(enter_row,enter_col)}
        queue = deque([(enter_row,enter_col,0)]) # row, col, steps
        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        while queue:
            row, col, steps = queue.popleft()
            for dx, dy in directions:
                new_row, new_col = row + dy, col + dx
                if valid(new_row, new_col) and (new_row, new_col) not in seen:
                    if is_exit(new_row, new_col):
                        return steps + 1

                    seen.add((new_row, new_col))
                    queue.append((new_row, new_col, steps + 1))
        return -1
        