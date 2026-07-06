class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        count0 = nums.count(0)
        if count0 == 0 or count0 == len(nums):
            return 0
        zero_place = nums[-count0:]
        misplacedNums = len(zero_place) - zero_place.count(0)
        return misplacedNums