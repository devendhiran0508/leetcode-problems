class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n=len(nums)
        result=-1
        premin=nums[0]
        for i in range(1,n):
            if nums[i]>premin:
                result=max(result,nums[i]-premin)
            else:
                premin=nums[i]
        return result