class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        value=[[i,nums[i]] for i in range(n)]
        value.sort(key =lambda x: -x[1])
        value=sorted(value[:k])
        result=[val for idx,val in value]
        return result