class Solution:
    def myPow(self, x: float, n: int) -> float:
        N = n
        if N < 0:
            x = 1 / x
            N = -N
        res = 1.0
        curr_pro = x
        while N > 0:
            if N % 2 == 1:
                res *= curr_pro
            curr_pro *= curr_pro
            N //= 2
        return res
