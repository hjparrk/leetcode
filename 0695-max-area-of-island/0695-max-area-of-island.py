from collections import defaultdict

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def is_valid(row, col):
            return 0 <= row < rows and 0 <= col <cols
        
        seen = set()
        directions = [[1,0],[-1,0],[0,-1],[0,1]] # up, down, left, right
        def dfs(row,col):
            area = 1
            seen.add((row,col))
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                if is_valid(new_row, new_col) and (new_row, new_col) not in seen and grid[new_row][new_col] == 1:
                    area += dfs(new_row, new_col)
            return area

        max_area = 0
        for row in range(rows):
            for col in range(cols):
                if (row,col) not in seen and grid[row][col] == 1:
                    area = dfs(row,col)
                    if area == 0:
                        max_area = max(max_area, 1)
                    else:
                        max_area = max(max_area, area)
        return max_area
        
        