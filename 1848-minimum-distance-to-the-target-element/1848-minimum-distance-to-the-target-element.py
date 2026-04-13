class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        for i, num in enumerate(nums):
            res = len(nums)
            if num == target:
                res = min(res, abs(i - start))
        return res
        