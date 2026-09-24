class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            sumDigit = 0
            while nums[i] != 0:
                sumDigit += nums[i] % 10
                nums[i] //= 10
            if sumDigit == i:
                return i
        return -1
        