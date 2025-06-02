class Solution:
    def myPow(self, x: float, n: int) -> float:
        def cal(x,n):
            if x==0:
                return 0
            if n==0:
                return 1
            result=cal(x,n//2)
            result=result*result
            if n%2==1:
                return result*x
            return result
        answer=cal(x,abs(n))
        if n>=0:
            return answer
        return 1/answer
        