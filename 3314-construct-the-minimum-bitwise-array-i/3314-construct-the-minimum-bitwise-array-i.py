class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        result=[]
        for num in nums:
            ori=num
            cand=-1
            for i in range(1,ori):
                if(i | (i+1)==ori):
                    cand=i
                    break
            result.append(cand)
        return result