class Solution:
    def maxDifference(self, s: str) -> int:
        a=Counter(s)
        odd=max(x for x in a.values() if x%2==1)
        even=min(x for x in a.values() if x%2==0)
        return odd-even