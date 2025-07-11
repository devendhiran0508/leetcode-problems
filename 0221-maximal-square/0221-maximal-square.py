class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows=len(matrix)
        cols=len(matrix[0])
        dp=[[0]*cols for _ in range(rows)]
        maxSide=0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]=="1":
                    if i==0 or j==0:
                        dp[i][j]=1
                    else:
                        dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                    maxSide=max(maxSide,dp[i][j])
        return maxSide*maxSide