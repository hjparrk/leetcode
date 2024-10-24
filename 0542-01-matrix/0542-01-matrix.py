from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n and mat[row][col] == 1

        m, n = len(mat), len(mat[0])

        seen = set()
        queue = deque()
        distances = [[0 for _ in range(n)] for _ in range(m)]

        for row in range(m):
            for col in range(n):
                if mat[row][col] == 0:
                    seen.add((row,col))
                    queue.append((row,col,1))
        
        directions = [(1,0), (0,1), (-1,0), (0,-1)] # top, right, bottom, left
        while queue:
            row, col, steps = queue.popleft()
            for dx, dy in directions:
                next_row, next_col = row + dy, col + dx
                if valid(next_row, next_col) and (next_row, next_col) not in seen:
                    seen.add((next_row, next_col))
                    queue.append((next_row, next_col, steps + 1))
                    distances[next_row][next_col] = steps
        return distances