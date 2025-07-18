class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        longitude=0
        latitude=0
        result=0
        n=len(s)
        for i in range(n):
            if s[i]=='N':
                latitude+=1
            elif s[i]=='S':
                latitude-=1
            elif s[i]=='W':
                longitude-=1
            elif s[i]=='E':
                longitude+=1
            result=max(result,min(abs(latitude)+abs(longitude)+k*2,i+1))
        return result