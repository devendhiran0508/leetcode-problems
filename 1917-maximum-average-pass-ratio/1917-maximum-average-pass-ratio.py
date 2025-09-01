class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def res(p,t):
            return (p+1)/(t+1)-p/t
        heap = [(-res(p, t), p, t) for p, t in classes]
        heapq.heapify(heap)
        for _ in range(extraStudents):
            g, p, t = heapq.heappop(heap)
            p, t = p + 1, t + 1
            heapq.heappush(heap, (-res(p, t), p, t))
        
        return sum(p/t for _, p, t in heap) / len(classes)