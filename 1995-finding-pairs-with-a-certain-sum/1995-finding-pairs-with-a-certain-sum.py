class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1=nums1
        self.nums2=nums2
        self.cnt=Counter(nums2)
        

    def add(self, index: int, val: int) -> None:
        oldVal=self.nums2[index]
        newVal=oldVal+val
        self.cnt[oldVal]-=1
        if self.cnt[oldVal]==0:
            del self.cnt[oldVal]
        self.nums2[index]=newVal
        self.cnt[newVal]+=1

        

    def count(self, tot: int) -> int:
        res=0
        for num in self.nums1:
            x=tot-num
            res+=self.cnt.get(x,0)
        return res



# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)