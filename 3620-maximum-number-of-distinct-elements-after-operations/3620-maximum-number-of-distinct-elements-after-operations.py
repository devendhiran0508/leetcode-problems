class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        count=0
        prev=-math.inf
        for num in nums:
            cur=min(max(num-k,prev+1),num+k)
            if cur>prev:
                count+=1
                prev=cur
        return count