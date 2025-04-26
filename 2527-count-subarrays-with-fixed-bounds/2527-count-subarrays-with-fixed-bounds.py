class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        count=0
        mini=-1
        maxi=-1
        left=-1
        for i in range(len(nums)):
            if nums[i]<minK or nums[i]>maxK:
                left=i
            if nums[i]==minK:
                mini=i
            if nums[i]==maxK:
                maxi=i
            count+=max(0,min(mini,maxi)-left)
        return count
        