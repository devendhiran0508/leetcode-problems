class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        for i in nums:
            n=len(str(i))
            if n%2==0:
                count+=1
        return count
        