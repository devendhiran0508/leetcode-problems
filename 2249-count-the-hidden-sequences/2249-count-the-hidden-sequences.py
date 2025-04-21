class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        a=0
        b=0
        cur=0
        for d in differences:
            cur+=d
            a=min(a,cur)
            b=max(b,cur)
            if b-a > upper-lower:
                return 0
        return (upper-lower)-(b-a)+1

        