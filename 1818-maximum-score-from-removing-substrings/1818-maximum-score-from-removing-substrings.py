class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x<y:
            s=s[::-1]
            x,y=y,x
        res=0
        stack1=[]

        for c in s:
            if stack1 and stack1[-1]=='a' and c=='b':
                stack1.pop()
                res+=x
            else:
                stack1.append(c)
        stack2=[]
        while stack1:
            c=stack1.pop()
            if stack2 and stack2[-1]=='a' and c=='b':
                stack2.pop()
                res+=y
            else:
                stack2.append(c)
        return res
