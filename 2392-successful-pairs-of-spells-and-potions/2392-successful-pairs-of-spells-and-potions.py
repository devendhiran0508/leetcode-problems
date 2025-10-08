class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res=[]
        n=len(potions)
        for s in spells:
            minNeed=(success+s-1)//s
            index=bisect.bisect_left(potions,minNeed)
            res.append(n-index)
        return res

