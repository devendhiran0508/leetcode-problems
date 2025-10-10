class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n=len(energy)
        res=-inf
        for i in range(n-k,n):
            tot=0
            j=i
            while j>=0:
                tot+=energy[j]
                res=max(res,tot)
                j-=k
        return res