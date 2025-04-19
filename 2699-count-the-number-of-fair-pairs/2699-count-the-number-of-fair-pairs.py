class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        return self.lower_bound(nums,upper+1)-self.lower_bound(nums,lower)

    def lower_bound(self,nums:List[int],value:int)->int:
        left=0
        right=len(nums)-1
        res=0
        while left<right:
            sum=nums[left]+nums[right]
            if sum<value:
                res+=right-left
                left+=1
            else:
                right-=1
        return res
    