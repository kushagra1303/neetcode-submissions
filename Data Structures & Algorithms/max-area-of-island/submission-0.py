class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        max_area = 0

        def dfs(r,c):
            if (r < 0 or c < 0 or r >= n or c >= m or grid[r][c] == 0):
                return 0
            grid[r][c] = 0
            area = 1

            area += dfs(r+1,c)
            area += dfs(r-1,c)
            area += dfs(r,c-1)
            area += dfs(r,c+1)
        
            return area

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    island_area = dfs(i,j)
                    max_area = max(max_area, island_area)

        return max_area        