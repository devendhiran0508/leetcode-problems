class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeroCount=0
        longWindow=0
        start=0
        for i in range(len(nums)):
            zeroCount+=(nums[i]==0)
            while(zeroCount>1):
                zeroCount-=(nums[start]==0)
                start+=1
            longWindow=max(longWindow,i-start)
        return longWindow