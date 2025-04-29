class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxElement=max(nums)
        start=0
        result=0
        maxWindow=0
        for i in range(len(nums)):
            if nums[i]==maxElement:
                maxWindow+=1
            while maxWindow==k:
                if nums[start]==maxElement:
                    maxWindow-=1
                start+=1
            result+=start
        return result

        