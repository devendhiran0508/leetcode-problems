class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n=len(nums)
        leftSum=0
        totalSum=sum(nums)
        for i in range(n):
            totalSum-=nums[i]
            if leftSum==totalSum:
                return i
            leftSum+=nums[i]
        return -1

        