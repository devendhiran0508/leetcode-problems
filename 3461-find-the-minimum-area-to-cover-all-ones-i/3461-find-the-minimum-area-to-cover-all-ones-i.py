class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        minI=n
        maxI=0
        minJ=m
        maxJ=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    minI=min(minI,i)
                    maxI=max(maxI,i)
                    minJ=min(minJ,j)
                    maxJ=max(maxJ,j)
        return (maxI-minI+1)*(maxJ-minJ+1)