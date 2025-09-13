class Solution:
    def maxFreqSum(self, s: str) -> int:
        word=Counter(s)
        vowel=max((word[ch] for ch in word if ch in "aeiou"),default=0)
        consonent=max((word[ch] for ch in word if ch not in "aeiou"),default=0)
        return vowel+consonent