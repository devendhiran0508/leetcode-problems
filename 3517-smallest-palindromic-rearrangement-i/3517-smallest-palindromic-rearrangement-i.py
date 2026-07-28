class Solution:
    def smallestPalindrome(self, s: str) -> str:
        k = len(s) // 2
        left = sorted(s[:k])
        mid = s[k] if len(s) % 2 != 0 else ""
        return "".join(left) + mid + "".join(left[::-1])