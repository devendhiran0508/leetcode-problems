class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        n=len(nums)
        def pairs(threshold):
            index,count=0,0
            while index<n-1:
                if nums[index+1]-nums[index]<=threshold:
                    count+=1
                    index+=1
                index+=1
            return count
        left=0
        right=nums[-1]-nums[0]
        while left<right:
            mid=left+(right-left)//2
            if pairs(mid)>=p:
                right=mid
            else:
                left=mid+1
        return left
        