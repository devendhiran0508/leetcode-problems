class Solution:
    def robotWithString(self, s: str) -> str:
        count=Counter(s)
        stack=[]
        result=[]
        minChar="a"
        for c in s:
            stack.append(c)
            count[c]-=1
            while minChar!="z" and count[minChar]==0:
                minChar=chr(ord(minChar)+1)
            while stack and stack[-1]<=minChar:
                result.append(stack.pop())
        return "".join(result)