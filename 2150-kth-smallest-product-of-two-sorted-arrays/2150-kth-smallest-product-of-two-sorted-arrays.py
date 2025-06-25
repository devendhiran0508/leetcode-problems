class Solution:
    def f(self,nums2,a,b):
        if a>0:
            return bisect_right(nums2,b//a)
        elif a<0:
            return len(nums2)-bisect_left(nums2,-(-b//a))
        else:
            return len(nums2) if b>=0 else 0
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n=len(nums1)
        left=-(10**10)
        right=(10**10)
        while left<=right:
            mid=(left+right)//2
            count=0
            for i in range(n):
                count+=self.f(nums2,nums1[i],mid)
            if count<k:
                left=mid+1
            else:
                right=mid-1
        return left