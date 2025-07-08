class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        n=len(events)
        dp=[[0]*(n+1) for _ in range(k+1)]
        events.sort()
        x=[start for start,end,value in events]
        for cur in range(n-1,-1,-1):
            for count in range(1,k+1):
                nextindex=bisect_right(x,events[cur][1])
                dp[count][cur]=max(dp[count][cur+1],events[cur][2]+dp[count-1][nextindex])
        return dp[k][0]
        