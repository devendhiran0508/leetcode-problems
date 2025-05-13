class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod=10**9+7
        alp=[0]*26
        for i in s:
            alp[ord(i)-ord("a")]+=1
        for j in range(t):
            nxt=[0]*26
            nxt[0]=alp[25]
            nxt[1]=(alp[25]+alp[0])%mod
            for i in range(2,26):
                nxt[i]=alp[i-1]
            alp=nxt
        result=sum(alp)%mod
        return result