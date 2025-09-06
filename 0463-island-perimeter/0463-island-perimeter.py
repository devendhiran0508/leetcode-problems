class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        res=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    res+=4
                    if i+1<m and grid[i+1][j]==1:
                        res-=2
                    if j+1<n and grid[i][j+1]==1:
                        res-=2
        return res