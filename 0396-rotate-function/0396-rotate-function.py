class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)

        present_F = sum(i * nums[i] for i in range(n))
        max_F = present_F

        for i in range(1,n):
            present_F = present_F + total - n * nums[n-i]
            max_F = max(max_F, present_F)
        return max_F