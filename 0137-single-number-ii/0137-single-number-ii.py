class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res=0
        for i in range(32):
            bitSum=0
            for num in nums:
                if(num>>i) & 1:
                    bitSum+=1
            if bitSum%3:
                res|=(1<<i)
        if res>=2**31:
            res-=2**32
        return res
        