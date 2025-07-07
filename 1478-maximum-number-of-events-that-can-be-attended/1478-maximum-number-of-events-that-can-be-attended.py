class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        i=0
        day=1
        res=0
        n=len(events)
        minHeap=[]
        while i <n or minHeap:
            while i<n and events[i][0]==day:
                heappush(minHeap,events[i][1])
                i+=1
            while minHeap and minHeap[0]<day:
                heappop(minHeap)
            if minHeap:
                heappop(minHeap)
                res+=1
            day+=1
        return res