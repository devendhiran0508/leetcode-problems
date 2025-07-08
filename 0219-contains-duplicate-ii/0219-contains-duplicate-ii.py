class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        res={}
        for i,num in enumerate(nums):
            if num in res and i-res[num]<=k:
                return True
            res[num]=i
        return False
            