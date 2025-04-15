class temp:
    def __init__(self,size):
        self.tree=[0]*(size+1)
    def update(self,index,delta):
        index+=1
        while index<len(self.tree):
            self.tree[index]+=delta
            index+=index & -index
    def query(self,index):
        index+=1
        result=0
        while index>0:
            result+=self.tree[index]
            index-=index & -index
        return result

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n=len(nums1)
        posInnums2={val: idx for idx, val in enumerate(nums2)}
        A=[posInnums2[val] for val in nums1]

        left=temp(n)
        leftsmall=[0]*n
        for i in range(n):
            leftsmall[i]=left.query(A[i]-1)
            left.update(A[i],1)
        
        right=temp(n)
        rightlarge=[0]*n
        for i in reversed(range(n)):
            rightlarge[i]=right.query(n-1)-right.query(A[i])
            right.update(A[i],1)

        good=sum(leftsmall[i]*rightlarge[i] for i in range(n))
        return good