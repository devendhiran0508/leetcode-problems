class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return nums
        mid=len(nums)//2
        left=self.sortArray(nums[:mid])
        right=self.sortArray(nums[mid:])
        return self.merge(left,right)

    def merge(self,left,right):
        i=j=0
        sortarray=[]
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                sortarray.append(left[i])
                i+=1
            else:
                sortarray.append(right[j])
                j+=1
        sortarray.extend(left[i:])
        sortarray.extend(right[j:])
        return sortarray