class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        num_set = set(nums)
        total = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                total += nums[i]
            else:
                break
        while total in num_set:
            total += 1
        return total