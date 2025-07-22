class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        a=set()
        left=0
        curSum=0
        maxSum=0
        for i in range(len(nums)):
            while nums[i] in a:
                a.remove(nums[left])
                curSum-=nums[left]
                left+=1
            a.add(nums[i])
            curSum+=nums[i]
            maxSum=max(curSum,maxSum)
        return maxSum