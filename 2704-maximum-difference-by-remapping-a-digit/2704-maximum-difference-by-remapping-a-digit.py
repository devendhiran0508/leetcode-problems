class Solution:
    def minMaxDifference(self, num: int) -> int:
        s=str(num)
        a=s
        val=0
        while val<len(s) and s[val]=="9":
            val+=1
        if val<len(s):
            s=s.replace(s[val],"9")
        a=a.replace(a[0],"0")
        return int(s)-int(a)
        