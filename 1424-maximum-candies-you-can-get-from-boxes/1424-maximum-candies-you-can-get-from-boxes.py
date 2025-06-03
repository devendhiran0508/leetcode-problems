class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        n=len(status)
        cand_open=[status[i]==1 for i in range(n)]
        hasbox=[False]*n
        used=[False]*n
        q=collections.deque()
        ans=0
        for box in initialBoxes:
            hasbox[box]=True
            if cand_open[box]:
                q.append(box)
                used[box]=True
                ans+=candies[box]
        while len(q)>0:
            bigbox=q.popleft()
            for key in keys[bigbox]:
                cand_open[key]=True
                if not used[key] and hasbox[key]:
                    q.append(key)
                    used[key]=True
                    ans+=candies[key]
            for box in containedBoxes[bigbox]:
                hasbox[box]=True
                if not used[box] and cand_open[box]:
                    q.append(box)
                    used[box]=True
                    ans+=candies[box]
        return ans