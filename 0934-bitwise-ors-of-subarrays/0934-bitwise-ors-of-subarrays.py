class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        res=set()
        cur=set()
        for num in arr:
            newCur={num}
            for prev in cur:
                newCur.add(prev|num)
            cur=newCur
            res.update(cur)
        return len(res)