class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        res=-1
        m=float('inf')
        n=len(edges)
        dist1=[-1]*n
        dist2=[-1]*n
        self.dfs(node1,0,edges,dist1)
        self.dfs(node2,0,edges,dist2)
        for i in range(n):
            if dist1[i]>=0 and dist2[i]>=0:
                maxdist=max(dist1[i],dist2[i])
                if maxdist<m:
                    m=maxdist
                    res=i
        return res
    def dfs(self,cur,dist,edges,distances):
        while cur!=-1 and distances[cur]==-1:
            distances[cur]=dist
            dist+=1
            cur=edges[cur]