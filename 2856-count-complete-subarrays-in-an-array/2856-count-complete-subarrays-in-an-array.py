class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n=len(nums)
        totalDistinct=len(set(nums))
        count={}
        result=0
        right=0
        for left in range(n):
            if left>0:
                count[nums[left-1]]-=1
                if count[nums[left-1]]==0:
                    del count[nums[left-1]]
            while right<n and len(count) < totalDistinct:
                count[nums[right]]=count.get(nums[right],0)+1
                right+=1
            if len(count)==totalDistinct:
                result+=n-right+1
        return result
