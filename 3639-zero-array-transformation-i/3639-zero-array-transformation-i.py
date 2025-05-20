class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        a=[0]*(len(nums)+1)
        for left,right in queries:
            a[left]+=1
            a[right+1]-=1
        count=[]
        curr=0
        for i in a:
            curr+=i
            count.append(curr)
        for j,k in zip(count,nums):
            if j<k:
                return False
        return True