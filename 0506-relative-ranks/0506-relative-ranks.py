class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n=len(score)
        res=[""]*n
        med=["Gold Medal","Silver Medal","Bronze Medal"]
        sortedScore=sorted([(s,i) for i,s in enumerate(score)], reverse=True)
        for rank,(s,i) in enumerate(sortedScore):
            if rank<3:
                res[i]=med[rank]
            else:
                res[i]=str(rank+1)
        return res