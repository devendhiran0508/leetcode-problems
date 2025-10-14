class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        count=1
        percent=0
        res=0
        for i in range(1,n):
            if nums[i]>nums[i-1]:
                count+=1
            else:
                percent,count=count,1
            res=max(res,min(percent,count))
            res=max(res,count//2)
        return res>=k