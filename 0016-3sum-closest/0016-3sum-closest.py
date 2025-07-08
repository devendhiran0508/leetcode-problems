class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n=len(nums)
        closeSum=float("inf")
        for i in range(n-2):
            left=i+1
            right=n-1
            while left<right:
                curSum=nums[i]+nums[left]+nums[right]
                if abs(curSum-target)< abs(closeSum-target):
                    closeSum=curSum
                if curSum<target:
                    left+=1
                elif curSum>target:
                    right-=1
                else:
                    return curSum
        return closeSum
        