class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        f=[[0]*k for _ in range(k)]
        res=0
        for num in nums:
            x=num%k
            for j in range(k):
                y=(j-x+k)%k
                f[x][y]=f[y][x]+1
                res=max(res,f[x][y])
        return res