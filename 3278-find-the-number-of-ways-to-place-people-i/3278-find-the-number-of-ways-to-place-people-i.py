class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda p: (p[0], -p[1]))
        ans = 0
        
        for i, (_, y1) in enumerate(points):
            max_y = -math.inf
            for _, y2 in points[i + 1:]:
                if y1 >= y2 > max_y:
                    ans += 1
                    max_y = y2
        return ans