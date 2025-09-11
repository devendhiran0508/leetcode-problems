class Solution:
    def sortVowels(self, s: str) -> str:
        vowels_set=set("aeiouAEIOU")
        vowelsSort=sorted([ch for ch in s if ch in vowels_set])
        res=[]
        i=0
        for ch in s:
            if ch in vowels_set:
                res.append(vowelsSort[i])
                i+=1
            else:
                res.append(ch)
        return "".join(res)