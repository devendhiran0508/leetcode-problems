class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        dire=[(1,1),(1,-1),(-1,1),(-1,-1)]
        nextVal={1:2,2:0,0:2}

        @cache
        def dfs(i,j,dirIdx,turned,val):
            if not(0<=i<m and 0<=j<n) or grid[i][j]!=val:
                return 0
            res=1
            nextI=i+dire[dirIdx][0]
            nextJ=j+dire[dirIdx][1]
            nxt=nextVal[val]
            res=max(res,1+dfs(nextI,nextJ,dirIdx,turned,nxt))

            if not turned:
                nd=(dirIdx+1)%4
                ti=i+dire[nd][0]
                tj=j+dire[nd][1]
                res=max(res,1+dfs(ti,tj,nd,True,nxt))
            return res
        ans=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    for k in range(4):ans=max(ans,dfs(i,j,k,False,1))
        return ans