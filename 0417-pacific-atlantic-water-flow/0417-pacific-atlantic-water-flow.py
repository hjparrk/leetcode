class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(row, col, seen):
            seen.add((row, col))
            for dx, dy in directions:
                new_row, new_col = row + dy, col + dx
                if (valid(new_row, new_col) and
                    (new_row, new_col) not in seen and
                    heights[new_row][new_col] >= heights[row][col]):
                    dfs(new_row, new_col, seen)

        pacific, atlantic = set(), set()
        for row in range(m):
            dfs(row, 0, pacific)
            dfs(row, n - 1, atlantic)

        for col in range(n):
            dfs(0, col, pacific)
            dfs(m - 1, col, atlantic)

        return list(pacific & atlantic)