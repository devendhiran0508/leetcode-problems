class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n=len(nums)
        result=0
        total=0
        i=0
        for j in range(n):
            total+=nums[j]
            while i<=j and total*(j-i+1)>=k:
                total-=nums[i]
                i+=1
            result+=j-i+1
        return result
        