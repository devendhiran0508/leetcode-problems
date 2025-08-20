class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        row=len(matrix)
        col=len(matrix[0])
        res=0
        dp=[[0]*(col+1) for _ in range(row+1)]
        for i in range(row):
            for j in range(col):
                if matrix[i][j]:
                    dp[i+1][j+1]=min(dp[i][j+1],dp[i+1][j],dp[i][j])+1
                    res+=dp[i+1][j+1]
        return res