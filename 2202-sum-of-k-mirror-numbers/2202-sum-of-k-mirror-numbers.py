class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def palindrome(x):
            digit=list()
            while x:
                digit.append(x%k)
                x//=k
            return digit==digit[::-1]
        left,count,result=1,0,0
        while count<n:
            right=left*10
            for i in [0,1]:
                for j in range(left,right):
                    if count==n:
                        break
                    combined=j
                    x=j//10 if i==0 else j
                    while x:
                        combined=combined*10+x%10
                        x//=10
                    if palindrome(combined):
                        count+=1
                        result+=combined
            left=right
        return result