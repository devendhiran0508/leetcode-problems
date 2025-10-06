class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[False] * n for _ in range(n)]
        pq = [(grid[0][0], 0, 0)] 
        visited[0][0] = True
        res = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        while pq:
            time, x, y = heapq.heappop(pq)
            res = max(res, time)
            if x == n-1 and y == n-1:
                return res
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    heapq.heappush(pq, (grid[nx][ny], nx, ny))
