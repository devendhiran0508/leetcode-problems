class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        minIdx = nums.index(min(nums))
        maxIdx = nums.index(max(nums))
        i = min(minIdx, maxIdx)
        j = max(minIdx, maxIdx)
        return min(j + 1, n - i, (i + 1) + (n - j))