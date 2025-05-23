class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n=len(nums)
        a=[[0]*2 for _ in range(n+1)]
        a[n][1]=0
        a[n][0]=-float('inf')
        for i in range(n-1,-1,-1):
            for j in range(2):
                opt=a[i+1][j^1]+(nums[i]^k)
                opt2=a[i+1][j]+nums[i]
                a[i][j]=max(opt,opt2)
        return a[0][1]