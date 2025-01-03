class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n

        dp = [[0 for _ in range(n)] for _ in range(m)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(row, col):
            if not dp[row][col]:
                max_len = 1
                for dx, dy in directions:
                    new_row, new_col = row + dy, col + dx
                    if valid(new_row, new_col) and\
                        matrix[new_row][new_col] > matrix[row][col]:
                        max_len = max(max_len, 1 + dfs(new_row, new_col))
                dp[row][col] = max_len

            return dp[row][col]
        
        ans = 0
        for row in range(m):
            for col in range(n):
                ans = max(ans, dfs(row, col))
        return ans