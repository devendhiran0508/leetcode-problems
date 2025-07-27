class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        a=[nums[0]]
        count=0
        for num in nums:
            if num!=a[-1]:
                a.append(num)
        for i in range(1,len(a)-1):
            if a[i]>a[i-1] and a[i]>a[i+1]:
                count+=1
            if a[i]<a[i-1] and a[i]<a[i+1]:
                count+=1
        return count
        