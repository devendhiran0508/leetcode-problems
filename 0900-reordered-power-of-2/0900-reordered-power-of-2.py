class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        nCount=Counter(str(n))
        for i in range(31):
            power=1<<i
            powerCount=Counter(str(power))
            if powerCount==nCount:
                return True
        return False