class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        adj=defaultdict(list)
        for a,b in zip(s1,s2):
            adj[a].append(b)
            adj[b].append(a)
        def dfs(c,visited):
            visited.add(c)
            minc=c
            for i in adj[c]:
                if i not in visited:
                    candidate=dfs(i,visited)
                    minc=min(minc,candidate)
            return minc
        result=[]
        for ch in baseStr:
            visited=set()
            result.append(dfs(ch,visited))
        return ''.join(result)
        