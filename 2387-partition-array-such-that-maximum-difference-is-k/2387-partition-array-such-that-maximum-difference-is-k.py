class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        result=1
        a=nums[0]
        for i in nums:
            if i-a>k:
                result+=1
                a=i
        return result