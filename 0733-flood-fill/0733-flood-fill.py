from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n, source_color = len(image), len(image[0]), image[sr][sc]
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n and image[row][col] == source_color
        image[sr][sc] = color
        seen = {(sr, sc)}
        queue = deque([(sr, sc)]) # row, col
        directions = [(1,0), (-1,0), (0,-1), (0, 1)]
        while queue:
            row, col = queue.popleft()
            for dx, dy in directions:
                new_row, new_col = row + dy, col + dx
                if valid(new_row, new_col) and (new_row, new_col) not in seen:
                    image[new_row][new_col] = color
                    seen.add((new_row, new_col))
                    queue.append((new_row, new_col))
        return image





        