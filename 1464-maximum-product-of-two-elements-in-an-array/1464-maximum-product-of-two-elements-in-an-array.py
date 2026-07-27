class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        big = 0
        secBig = 0
        for num in nums:
            if num > big:
                secBig = big
                big = num
            else:
                secBig = max(secBig, num)
        return (big - 1) * (secBig - 1)