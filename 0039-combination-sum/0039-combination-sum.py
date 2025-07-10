class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def makeComb(index,comb,total):
            if total==target:
                res.append(comb[:])
                return
            if total>target or index>=len(candidates):
                return
            comb.append(candidates[index])
            makeComb(index,comb,total+candidates[index])
            comb.pop()
            makeComb(index+1,comb,total)
            return res
        return makeComb(0,[],0)