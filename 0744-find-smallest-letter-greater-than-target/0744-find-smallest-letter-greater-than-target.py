class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        res=letters[0]
        flag=False
        for c in letters:
            if not flag:
                if c>target:
                    res=c
                    flag=not flag
            else:
                if c>target and c<res:
                    res=c
        return res