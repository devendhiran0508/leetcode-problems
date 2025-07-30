class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxVal=0
        res=0
        curStreak=0
        for num in nums:
            if maxVal<num:
                maxVal=num
                res=0
                curStreak=0
            if maxVal==num:
                curStreak+=1
            else:
                curStreak=0
            res=max(res,curStreak)
        return res