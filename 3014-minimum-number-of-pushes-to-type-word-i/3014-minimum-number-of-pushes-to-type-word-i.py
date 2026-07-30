class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        push = 0
        push += min(n, 8) * 1
        if (n > 8):
            push += min(n - 8, 8) * 2
        if (n > 16):
            push += min(n - 16, 8) * 3
        if (n > 24):
            push += min(n - 24, 8) * 4
        return push