class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[1]*n
        last=[-1]*32

        for i in range(n-1,-1,-1):
            t=1
            for j in range(32):
                if(nums[i]>>j) &1:
                    last[j]=i
                elif last[j]!=-1:
                    t=max(t,last[j]-i+1)
            res[i]=t
        return res