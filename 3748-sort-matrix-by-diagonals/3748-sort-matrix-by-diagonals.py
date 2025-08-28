class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n=len(grid)
        for i in range(n):
            temp=[grid[i+j][j] for j in range(n-i)]
            temp.sort(reverse=True)
            for j in range(n-i):
                grid[i+j][j]=temp[j]
        for j in range(1,n):
            temp=[grid[i][j+i] for i in range(n-j)]
            temp.sort()
            for i in range(n-j):
                grid[i][j+i]=temp[i]
        return grid
