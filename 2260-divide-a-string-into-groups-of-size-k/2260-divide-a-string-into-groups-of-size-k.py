class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        result=[]
        n=len(s)
        startIndex=0
        while startIndex<n:
            result.append(s[startIndex:startIndex+k])
            startIndex+=k
        result[-1]+=fill*(k-len(result[-1]))
        return result