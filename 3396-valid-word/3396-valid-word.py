class Solution:
    def isValid(self, word: str) -> bool:
        n=len(word)
        if n<3:
            return False
        hasVowel=False
        hasConsonant=False
        for c in word:
            if c.isalpha():
                if c.lower() in 'aeiou':
                    hasVowel=True
                else:
                    hasConsonant=True
            elif not c.isdigit():
                return False
        return hasVowel and hasConsonant

        