class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for x in nums:
            idx=abs(x)-1
            if nums[idx]>0:
                nums[idx]*=-1
        res=[]
        for i,val in enumerate(nums):
            if val>0:
                res.append(i+1)
        return res

        #using hashset
        # n=len(nums)
        # return list(set(range(1,n+1))-set(nums))