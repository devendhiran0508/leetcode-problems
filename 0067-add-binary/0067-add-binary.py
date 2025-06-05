class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sumDec=int(a,2)+int(b,2)
        return bin(sumDec)[2:]
    
        