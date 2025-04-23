class Solution:
    def countLargestGroup(self, n: int) -> int:
        count={}
        for i in range(1,n+1):
            digitsum=sum(int(digit) for digit in  str(i))
            if digitsum in count:
                count[digitsum]+=1
            else:
                count[digitsum]=1
        maxvalue=max(count.values())
        larger=sum(1 for v in count.values() if v==maxvalue)
        return larger
        