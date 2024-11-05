from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n and mat[row][col] == 1
        
        seen = set()
        queue = deque()
        for row in range(m):
            for col in range(n):
                if mat[row][col] == 0:
                    queue.append((row, col, 0))
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        while queue:
            row, col, steps = queue.popleft()
            for dx, dy in directions:
                new_row, new_col = row + dy, col + dx
                if valid(new_row, new_col) and (new_row, new_col) not in seen:
                    seen.add((new_row, new_col))
                    queue.append((new_row, new_col, steps + 1))
                    mat[new_row][new_col] = steps + 1
        return mat

