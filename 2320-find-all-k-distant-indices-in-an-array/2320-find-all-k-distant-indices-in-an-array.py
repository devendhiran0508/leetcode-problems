class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        result=[]
        n=len(nums)
        for i in range(n):
            for j in range(n):
                if nums[j]==key and abs(i-j)<=k:
                    result.append(i)
                    break
        return result