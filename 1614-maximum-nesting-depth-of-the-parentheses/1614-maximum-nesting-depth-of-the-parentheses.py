class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0
        openBrac = 0
        for c in s:
            if c == '(':
                openBrac += 1
            if c == ')':
                openBrac -= 1
            res = max(res, openBrac)  
        return res 