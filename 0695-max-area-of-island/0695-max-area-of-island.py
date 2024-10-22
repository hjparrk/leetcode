from collections import defaultdict

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        graph = defaultdict(list)
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    node = (row,col)
                    up, down, left, right = (row-1,col), (row+1,col), (row,col-1), (row,col+1)

                    if row - 1 >= 0 and grid[row-1][col] == 1:
                        graph[node].append(up)

                    if row + 1 < m and grid[row+1][col] == 1:
                        graph[node].append(down)

                    if col - 1 >= 0 and grid[row][col-1]:
                        graph[node].append(left)

                    if col + 1 < n and grid[row][col+1]:
                        graph[node].append(right)

        seen = set()
        def dfs(node):
            area = 0
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    area += 1 + dfs(neighbor)
            return area
        
        ans = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    area = 0
                    if graph[(row,col)]:
                        area = dfs((row,col))
                    else:
                        area = 1
                    ans = max(ans, area)

        return ans
        