class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]
        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visited[i][j]:
                    count += 1
                    stack = [(i, j)]
                    visited[i][j] = True

                    while stack:
                        r, c = stack.pop()

                        for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                            if 0 <= nr < m and 0 <= nc < n:
                                if grid[nr][nc] == "1" and not visited [nr][nc]:
                                    visited[nr][nc] = True
                                    stack.append((nr, nc))

        return count
        