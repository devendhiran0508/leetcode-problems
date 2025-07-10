class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        count=1
        prev=nums[0]
        n=len(nums)
        for i in range(n):
            if nums[i]!=prev:
                count+=1
                prev=nums[i]
            if count==3:
                return nums[i]
        return nums[0]
        