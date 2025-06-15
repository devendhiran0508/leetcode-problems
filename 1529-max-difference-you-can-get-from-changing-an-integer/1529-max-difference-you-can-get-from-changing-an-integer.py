class Solution:
    def maxDiff(self, num: int) -> int:
        def swap(x,y):
            return str(num).replace(str(x),str(y))
        minNum=num
        maxNum=num
        for x in range(10):
            for y in range(10):
                result=swap(x,y)
                if result[0]!="0":
                    result1=int(result)
                    minNum=min(minNum,result1)
                    maxNum=max(maxNum,result1)
        return maxNum-minNum
        