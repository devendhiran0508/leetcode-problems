class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combinedArray=nums1+nums2
        combinedArray.sort()
        n=len(combinedArray)
        if(n%2==0):
            median=(combinedArray[n//2-1] + combinedArray[n//2])/2
        else:
            median=combinedArray[n//2]
        return median