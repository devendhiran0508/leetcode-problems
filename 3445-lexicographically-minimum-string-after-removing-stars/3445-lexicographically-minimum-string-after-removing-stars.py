class Solution:
    def clearStars(self, s: str) -> str:
        count=[[] for _ in range(26)]
        a=list(s)
        for i,c in enumerate(a):
            if c!="*":
                count[ord(c)-ord("a")].append(i)
            else:
                for j in range(26):
                    if count[j]:
                        a[count[j].pop()]="*"
                        break
        return "".join(c for c in a if c!="*") 