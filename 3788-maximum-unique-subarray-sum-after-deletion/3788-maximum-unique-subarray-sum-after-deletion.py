class Solution:
    def maxSum(self, nums: List[int]) -> int:
        maxi=max(nums)
        if maxi<=0:
            return maxi
        res=0
        a=set()
        for i in nums:
            if i>=0 and i not in a:
                res+=i
                a.add(i)
        return res
        