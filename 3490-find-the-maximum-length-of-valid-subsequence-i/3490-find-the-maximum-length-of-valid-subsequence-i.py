class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        allEven=allOdd=altEvenOdd=altOddEven=0
        for n in nums:
            if n%2==0:
                allEven+=1
                altEvenOdd=altOddEven+1
            else:
                allOdd+=1
                altOddEven=altEvenOdd+1
        return max(allEven,allOdd,altEvenOdd,altOddEven)
        