class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return '1'
        def run_length(s:str)->str:
            result=''
            i=0
            while i<len(s):
                count=1
                while i+1<len(s) and s[i]==s[i+1]:
                    i+=1
                    count+=1
                result+=str(count)+s[i]
                i+=1
            return result
        cur='1'
        for _ in range(1,n):
            cur=run_length(cur)
        return cur
        