class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        a=[]
        curr=1
        for _ in range(n):
            a.append(curr)
            if curr*10<=n:
                curr*=10
            else:
                while curr%10==9 or curr>=n:
                    curr//=10
                curr+=1
        return a
        