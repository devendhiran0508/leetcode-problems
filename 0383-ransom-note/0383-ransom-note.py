class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ranCount=Counter(ransomNote)
        magCount=Counter(magazine)
        for char in ranCount:
            if ranCount[char]>magCount[char]:
                return False
        return True
        