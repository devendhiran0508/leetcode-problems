class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        count=defaultdict(int)
        for i in word:
            count[i]+=1
        result=len(word)
        for a in count.values():
            delete=0
            for b in count.values():
                if a>b:
                    delete+=b
                elif b>a+k:
                    delete+=b-(a+k)
            result=min(result,delete)
        return result