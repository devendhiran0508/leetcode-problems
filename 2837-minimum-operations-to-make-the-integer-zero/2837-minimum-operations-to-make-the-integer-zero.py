class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for k in range(1,60):
            val=num1-k*num2
            if val<0:
                return -1
            if bin(val).count("1")<=k<=val:
                return k
                