class Solution:
    def makeFancyString(self, s: str) -> str:
        pre=s[0]
        fre=1
        res=s[0]
        for i in range(1,len(s)):
            if s[i]==pre:
                fre+=1
            else:
                pre=s[i]
                fre=1
            if fre<3:
                res+=s[i]
        return res
        