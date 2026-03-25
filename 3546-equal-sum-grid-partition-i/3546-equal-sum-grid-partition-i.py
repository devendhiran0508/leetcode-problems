class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m=len(grid)
        n=len(grid[0])
        total = sum(sum(row) for row in grid)

        if total%2!=0:
            return False
        target = total//2

        row_sum=0
        for i in range(m-1):
            row_sum+=sum(grid[i])
            if row_sum==target:
                return True
        col_sum=0
        for j in range(n-1):
            for i in range(m):
                col_sum+=grid[i][j]
            if target==col_sum:
                return True
        return False
        