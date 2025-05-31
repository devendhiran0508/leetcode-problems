class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n=len(board)
        minRoll=[-1]*(n*n+1)
        q=deque()
        minRoll[1]=0
        q.append(1)
        while q:
            x=q.popleft()
            for i in range(1,7):
                t=x+i
                if t>n*n:
                    break
                row=(t-1)//n
                col=(t-1)%n
                v=board[n-1-row][(n-1-col)if(row%2==1)else col]
                y=v if v>0 else t
                if y==n*n:
                    return minRoll[x]+1
                if minRoll[y]==-1:
                    minRoll[y]=minRoll[x]+1
                    q.append(y)
        return -1