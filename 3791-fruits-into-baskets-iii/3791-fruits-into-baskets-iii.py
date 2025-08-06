class SegmentTree:
    def __init__(self,arr):
        self.n=len(arr)
        self.tree=[0]*(4*self.n)
        self.build(arr,0,self.n-1,1)
    
    def build(self,arr,l,r,idx):
        if l==r:
            self.tree[idx]=arr[l]
            return 
        mid=(l+r)//2
        self.build(arr,l,mid,2*idx)
        self.build(arr,mid+1,r,2*idx+1)
        self.tree[idx]=max(self.tree[2*idx],self.tree[2*idx+1])
    
    def queryFirst(self,target,l,r,idx):
        if self.tree[idx]<target:
            return -1
        if l==r:
            self.tree[idx]=-1
            return l
        mid=(l+r)//2
        if self.tree[2*idx]>=target:
            res=self.queryFirst(target,l,mid,2*idx)
        else:
            res=self.queryFirst(target,mid+1,r,2*idx+1)
        self.tree[idx]=max(self.tree[2*idx],self.tree[2*idx+1])
        return res

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n=len(baskets)
        st=SegmentTree(baskets)
        unplaced=0

        for fruit in fruits:
            pos=st.queryFirst(fruit,0,n-1,1)
            if pos==-1:
                unplaced+=1
        return unplaced