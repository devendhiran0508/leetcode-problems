class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        dire = [(1,1),(1,-1),(-1,-1),(-1,1)]
        m, n = len(grid), len(grid[0])

        @cache
        def dfs(i, j, dirIdx, turned, val):
            ni, nj = i + dire[dirIdx][0], j + dire[dirIdx][1]
            if not (0 <= ni < m and 0 <= nj < n) or grid[ni][nj] != val:
                return 0
            res = dfs(ni, nj, dirIdx, turned, 2 - val)
            if turned:
                res = max(res, dfs(ni, nj, (dirIdx + 1) % 4, False, 2 - val))
            return res + 1

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for k in range(4):
                        ans = max(ans, 1 + dfs(i, j, k, True, 2))
        return ans